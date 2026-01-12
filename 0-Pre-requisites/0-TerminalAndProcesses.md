# Introduction to the Terminal and the Notion of Processes (PowerShell and Linux Shell Edition)

Throughout these tutorial materials you will often have to run processes, so follow the instructions below carefully and use the web to learn more about them.

## What is the Terminal?

The **terminal** (also known as the command line or shell) is a text-based interface that allows you to interact with your computer by typing commands.

- In **Windows**, the terminal is usually **PowerShell**.
- In **Linux**, the terminal uses shells like **bash** or **zsh**.

It lets you **navigate folders**, **run programs as processes**, and **manage files**.

### Basic Commands

Open your terminal application and execute the following commands along.

```powershell
# Show current directory
# PowerShell:
pwd
# Linux:
pwd
```

```powershell
# Change to a specific directory (for example, Documents)
# PowerShell:
Set-Location -Path "$HOME\Downloads"
# Linux:
cd ~/Downloads
```

```powershell
# List files and folders
# PowerShell:
Get-ChildItem
# Linux:
ls
```

```powershell
# Make a new folder called "my_folder"
# PowerShell:
New-Item -ItemType Directory -Name "my_folder"
# Linux:
mkdir my_folder
```

```powershell
# Check that it was created
# PowerShell:
Get-ChildItem
# Linux:
ls
```

```powershell
# Remove the folder
# PowerShell:
Remove-Item -Recurse -Force .\my_folder
# Linux:
rm -r my_folder
```

## What is a Process?

A **process** is a running instance of a program. When you open an app or run a command, your computer creates a process for it.

Each process:
- Takes up some memory
- Can run for a long or short time
- Can create other processes (called "child processes")

Think of a process like a person doing a task — your computer can have many people (processes) working at the same time.

### Example: Running Two Python Scripts in Separate Terminals

Let's explore processes by running two Python scripts at the same time in different terminals.

1. **Create two simple Python scripts:**

    Create a file called `script1.py`:
    ```python
    # script1.py
    import time
    while True:
        print("Running script 1...")
        time.sleep(2)
    ```

    Create a file called `script2.py`:
    ```python
    # script2.py
    import time
    while True:
        print("Running script 2...")
        time.sleep(2)
    ```

2. **Open two terminal windows and and change directory to the same as the scripts:**
   - In **PowerShell**, run:
     ```powershell
     python script1.py
     ```
     (in one terminal)
     
     ```powershell
     python script2.py
     ```
     (in another terminal)

   - In **Linux**, use:
     ```bash
     python3 script1.py
     ```
     and
     ```bash
     python3 script2.py
     ```

    You can terminate these processes at any time by typing `Ctrl+c` in the corresponding terminal.

3. **Open a third terminal window** to inspect the processes, or open your task manager to inspect them:
   - PowerShell:
     ```powershell
     Get-Process | Where-Object { $_.Name -like "*python*" }
     ```
   - Linux:
     ```bash
     ps aux | grep python
     ```

    Observe how each script runs as its own process.

### Inspecting Processes in Task Manager (Windows)

You can also observe these processes using the **Windows Task Manager**:

1. **Open Task Manager**:
   - Right-click the taskbar and select **Task Manager**, or press `Ctrl + Shift + Esc`.
   - Make sure the **Processes** tab is selected on the left. This view shows the list of active processes.
   - Look for `python.exe` — you should see two entries if both scripts are running. Type python in the search bar if needed.

2. **Add the 'Command line' column**:
   - Right-click on any column header (e.g., "Name"), and enable **Command line**.
   - You will now see the full command used to start each Python script (including the filename).

### Inspecting Processes with System Monitor (or htop)

1. **Using System Monitor (GNOME)**:
   - Press `Super` (Windows key) and search for **System Monitor**, then open it.
   - Go to the **Processes** tab.
   - Look for entries labeled `python3`. There should be two if both scripts are running.
   - Right-click a process and choose **Properties** to view details, including the command line.

2. **Using `htop` (advanced, terminal-based)**:
   - Open a terminal and run:
     ```bash
     htop
     ```
     If not installed, you can install it using:
     ```bash
     sudo apt install htop   # Debian/Ubuntu
     sudo dnf install htop   # Fedora
     ```
   - Look for `python3` entries.
   - Use the arrow keys to navigate and press `F1` for help or `F10` to exit.

This is useful to identify which script is doing what, especially when running multiple similar processes.

### Running Shell Commands from Jupyter Notebooks

Jupyter Notebooks support running shell (terminal) commands directly in code cells. This allows you to interact with the operating system without leaving the notebook.

To do this, simply prefix the command with an exclamation mark `!`.

#### Examples

```python
# List files in the current directory
!ls              # Linux
!Get-ChildItem   # PowerShell (Windows)
```

```python
# Check current working directory
!pwd             # Linux or PowerShell
```

```python
# Create a folder
!mkdir test_folder        # Linux
!New-Item -ItemType Directory -Name "test_folder"  # PowerShell
```

```python
# Remove a folder
!rm -r test_folder        # Linux
!Remove-Item -Recurse -Force .\test_folder  # PowerShell
```

You can use this feature to experiment with terminal commands and observe their effects directly within your notebook environment.
