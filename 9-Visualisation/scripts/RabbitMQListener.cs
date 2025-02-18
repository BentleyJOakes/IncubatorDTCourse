using Godot;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;
using System;
using System.Collections.Generic;
using System.Text;

public partial class RabbitMQListener : Node
{
	private ConnectionFactory factory = new ConnectionFactory();
	private IConnection connection;
	private IModel channel;

	private string exchangeName = "Incubator_AMQP";
	private string ROUTING_KEY_KF_PLANT_STATE = "incubator.record.kalmanfilter.plant.state";
	private string ROUTING_KEY_STATE = "incubator.record.driver.state";
	private string localQueue;
	private List<string> messages = new();

	private string userName = "incubator";
	private string hostName = "localhost";
	private string password = "incubator";
	private string port = "5672";

	[Signal]
	public delegate void OnMessageEventHandler(string message);

	public override void _Ready()
	{
		if (userName != "") {
			factory.UserName = userName;
			GD.Print("Host name set to: " + userName);
		}

		if (hostName != "") {
			GD.Print("Host name set to: " + hostName);
		} 

		if (password != "") {
			factory.Password = password;
			GD.Print("Password set to: " + password);
		} 

		if (port != "") {
			factory.Port = port.ToInt();
			GD.Print("Port set to: " + port);
		} 
		else {
			factory.Port = 5672;
			GD.Print("Port not set, using default: 5672");
		}

		connection = factory.CreateConnection();
		channel = connection.CreateModel();
		
		localQueue = channel.QueueDeclare(autoDelete: true, exclusive: true); 
		channel.QueueBind(queue: localQueue, exchange: exchangeName, routingKey: ROUTING_KEY_KF_PLANT_STATE);
		channel.QueueBind(queue: localQueue, exchange: exchangeName, routingKey: ROUTING_KEY_STATE);
		ReceiveMessage();
		
		if (!connection.IsOpen) {
			GD.Print("Error! Could not connect!");
		}
		else {
			GD.Print("Connection established");
		}
	}

	public override void _Process(double delta) {
		for (int i = 0; i < messages.Count; i++) {
			EmitSignal(SignalName.OnMessage, messages[i]);
		}
		messages.Clear();
	}

	private void ReceiveMessage() {
		GD.Print("Waiting for messages");
		var consumer = new EventingBasicConsumer(channel);

		consumer.Received += (model, ea) => {
			var body = ea.Body.ToArray();
			var message = Encoding.ASCII.GetString(body);
			messages.Add(message);
		};

		channel.BasicConsume(queue: localQueue, autoAck: true, consumer: consumer);
	}
}
