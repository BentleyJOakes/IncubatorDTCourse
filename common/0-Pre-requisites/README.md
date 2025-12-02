# Prerequisites

Here’s a quick guide to set up the prerequisites: **Anaconda**, **Python**, **Git**, and **Jupyter Notebook**. If you already have these installed, you can skip ahead to the next steps.

### Step 1: Install Conda

First, you need to install **Conda**. Conda is a powerful package manager that helps you manage environments and dependencies.

Follow the official installation instructions:
[Conda Installation Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

Choose the appropriate version for your operating system (Windows, macOS, Linux) and follow the setup steps.

### Step 2: Create a Python Environment

After installing Conda, you’ll create a new environment with Python.

1. Open your terminal (or Anaconda Prompt on Windows).
2. Run the following command to create a new environment named `DTcourse`:

   ```bash
   conda create -n DTcourse python
   ```

3. Once the environment is created, activate it by running:

   ```bash
   conda activate DTcourse
   ```

4. Verify the Python version by running:

   ```bash
   python --version
   ```

   Ensure that the Python version matches the required version for the project.

### Step 3: Install Git

You’ll also need **Git** for version control and to clone the project repository.

1. Install Git within the Conda environment:

   ```bash
   conda install git
   ```

2. Verify the Git installation by running:

   ```bash
   git --version
   ```

   This will display the installed version of Git.

### Step 4: Clone the GitHub Repository

Now that you have Git installed, you can clone the project repository to your local machine.

1. In your terminal, navigate to the directory where you want to store the project.
2. Run the following command to clone the repository:

   ```bash
   git clone https://github.com/BentleyJOakes/IncubatorDTCourse
   ```

3. Navigate to the project directory:

   ```bash
   cd IncubatorDTCourse
   ```

### Step 5: Install Jupyter Notebook

**Jupyter Notebook** is required to run and interact with the project’s `.ipynb` files.

1. Install Jupyter Notebook in the current environment by running:

   ```bash
   conda install notebook
   ```

2. Verify the installation by checking the version:

   ```bash
   jupyter --version
   ```

3. Start Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

   This will open a new tab in your web browser, displaying the Jupyter interface. Be sure to run this command from within the project directory (`IncubatorDTCourse`).

### Step 6: Running the Notebooks

Once Jupyter Notebook has started, you can open and run the provided `.ipynb` notebooks. These notebooks contain the instructions and code to guide you through the course.