
# Ignore this: just a bunch of functions to load and enhance the data
import math
import pandas
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def from_ns_to_s(time_ns):
    return time_ns / 1e9

def convert_time_s_to_ns(timeseries):
    return timeseries.map(lambda time_ns: from_ns_to_s(time_ns))

def load_timestamped_data(filepath, desired_timeframe, time_unit, normalize_time, convert_to_seconds):
    realpath = filepath
    csv = pandas.read_csv(realpath)

    start_idx = 0
    while start_idx < len(csv) and csv.iloc[start_idx]["time"] < desired_timeframe[0]:
        start_idx = start_idx + 1

    end_idx = len(csv["time"]) - 1
    while end_idx > 0 and csv.iloc[end_idx]["time"] > desired_timeframe[1]:
        end_idx = end_idx - 1

    if end_idx <= start_idx:
        print(
            f"Warning: after trimming ended up with start_idx={start_idx} and end_idx={end_idx}. This results in empty data")
        return None

    indices = range(start_idx, end_idx + 1)
    csv = csv.iloc[indices]

    csv["timestamp_ns"] = pandas.to_datetime(csv["time"], unit=time_unit)
    # normalize time
    if normalize_time:
        csv["time"] = csv["time"] - csv.iloc[0]["time"]
    # Convert time
    if convert_to_seconds and time_unit != 's':
        assert time_unit == 'ns', "Other time units not supported."
        csv["time"] = convert_time_s_to_ns(csv["time"])

    return csv


def convert_event_to_signal(time, events, categories, start):
    """
    Takes event data, that looks like this:
        time,event,code
        1614861060000000000,"Lid Opened", "lid_open"
        1614861220000000000,"Lid Closed", "lid_close"
    And produces a piecewise constant signal, where the values are given by the categories map.
    """
    last_value = categories[start]
    event_idx = 0
    signal = []
    for t in time:
        if event_idx < len(events) and t >= events.iloc[event_idx]["time"]:
            last_value = categories[events.iloc[event_idx]["code"]]
            event_idx += 1
        signal.append(last_value)

    assert len(signal) == len(time)

    return signal


def derive_data(data, heater_voltage, heater_current, events=None):
    data["power_in"] = data.apply(lambda row: heater_voltage * heater_current if row.heater_on else 0.0, axis=1)

    data["average_temperature"] = data.apply(lambda row: np.mean([row.t2, row.t3]), axis=1)
    zero_kelvin = 273.15
    data["avg_temp_kelvin"] = data["average_temperature"] + zero_kelvin
    air_mass = 0.04  # Kg
    air_heat_capacity = 700  # (j kg^-1 °K^-1)

    data["potential_energy"] = data["avg_temp_kelvin"] * air_mass * air_heat_capacity
    data["potential_energy"] = data["potential_energy"] - data.iloc[0]["potential_energy"]

    if events is not None:
        lid_events = events.loc[(events["code"] == "lid_close") | (events["code"] == "lid_open")]
        data["lid_open"] = convert_event_to_signal(data["time"], lid_events, categories={"lid_close": 0.0, "lid_open": 1.0},
                                                  start="lid_close")
    else:
        data["lid_open"] = 0.0

    return data

def load_data(filepath, heater_voltage, heater_current, events=None, desired_timeframe=(- math.inf, math.inf), time_unit='s', normalize_time=True, convert_to_seconds=False):
    data = load_timestamped_data(filepath, desired_timeframe, time_unit, normalize_time, convert_to_seconds)
    event_data = None
    if events is not None:
        assert not normalize_time, "Not allowed to normalize data with events."
        event_data = load_timestamped_data(events, desired_timeframe, time_unit, normalize_time, convert_to_seconds)

    return derive_data(data, heater_voltage, heater_current, events=event_data), event_data


def plotly_incubator_data(data, compare_to=None, heater_T_data=None, events=None,
                          overlay_heater=True, show_actuators=False, show_sensor_temperatures=False,
                          show_hr_time=False):
    nRows = 2
    titles = ["Incubator Temperature (°C)", "Room Temperature (°C)"]
    if show_actuators:
        nRows += 1
        titles.append("Actuators")
    if heater_T_data is not None:
        nRows += 1
        titles.append("Heatbed Temperature (°C)")

    x_title = "Timestamp" if show_hr_time else "Time (s)"

    time_field = "timestamp_ns" if show_hr_time else "time"

    fig = make_subplots(rows=nRows, cols=1, shared_xaxes=True,
                        x_title=x_title,
                        subplot_titles=titles)

    if show_sensor_temperatures:
        fig.add_trace(go.Scatter(x=data[time_field], y=data["t2"], name="t2 (right)"), row=1, col=1)
        fig.add_trace(go.Scatter(x=data[time_field], y=data["t3"], name="t3 (top)"), row=1, col=1)

    fig.add_trace(go.Scatter(x=data[time_field], y=data["average_temperature"], name="avg_T"), 
                  row=1, col=1)
    if overlay_heater:
        fig.add_trace(go.Scatter(x=data[time_field], y=[40 if b else 30 for b in data["heater_on"]], name="heater_on"), row=1, col=1)

    if events is not None:
        for i, r in events.iterrows():
            # Get the closest timestamp_ns to the event time
            closest_ts = min(data[time_field], key=lambda x:abs(x-r[time_field]))
            # Get the average temperature for that timestamp_ns
            avg_temp = data.iloc[data.index[data[time_field] == closest_ts]]["average_temperature"].iloc[0]

            fig.add_annotation(x=r[time_field], y=avg_temp,
                               text=r["event"],
                               showarrow=True,
                               arrowhead=1)

    if compare_to is not None:
        for res in compare_to:
            if "T" in compare_to[res]:
                fig.add_trace(go.Scatter(x=compare_to[res][time_field], 
                                         y=compare_to[res]["T"],
                                         error_y={
                                            "type" : 'data',
                                            "array" : compare_to[res]["T_std_dev"] if "T_std_dev" in compare_to[res] else None,
                                         },
                                         name=f"avg_temp({res})"), row=1, col=1)
            if "T_object" in compare_to[res]:
                fig.add_trace(go.Scatter(x=compare_to[res][time_field], y=compare_to[res]["T_object"], name=f"T_object({res})"), row=1, col=1)

    fig.add_trace(go.Scatter(x=data[time_field], y=data["t1"], name="room"), 
                  row=2, col=1)

    next_row = 3

    if show_actuators:
        fig.add_trace(go.Scatter(x=data[time_field], y=data["heater_on"], name="heater_on"), row=next_row, col=1)
        fig.add_trace(go.Scatter(x=data[time_field], y=data["fan_on"], name="fan_on"), row=next_row, col=1)

        if compare_to is not None:
            for res in compare_to:
                if "in_lid_open" in compare_to[res]:
                    fig.add_trace(go.Scatter(x=compare_to[res][time_field], y=compare_to[res]["in_lid_open"], name=f"in_lid_open({res})"), row=next_row, col=1)

        next_row += 1

    if heater_T_data is not None:
        for trace in heater_T_data:
            fig.add_trace(go.Scatter(x=heater_T_data[trace][time_field], y=heater_T_data[trace]["T_heater"],
                                     name=f"T_heater({trace})", 
                                     error_y={
                                        "type" : 'data',
                                        "array" : heater_T_data[trace]["T_heater_std_dev"] if "T_heater_std_dev" in heater_T_data[trace] else None,
                                    }
                                    ), 
                                    row=next_row, col=1)
        next_row += 1

    fig.update_layout()

    return fig

