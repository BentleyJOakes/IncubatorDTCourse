# Incubator Digital Twin Course

This repository hosts the materials to provide a step-by-step guide the reader into building a digital twin (DT) for the [incubator project](https://github.com/INTO-CPS-Association/example_digital-twin_incubator).

This repository is divided into ordered modules. Each module is in a separate folder, containing one or more Jupyter notebooks. It is **strongly recommended that modules and Jupyter notebooks are followed in order**, as they sometimes depend on each other.

## Contents
- [Incubator Digital Twin Course](#incubator-digital-twin-course)
  - [Contents](#contents)
  - [Questions and Issues](#questions-and-issues)
  - [Pre-Requisites](#pre-requisites)
    - [Git](#git)
    - [Python](#python)
    - [VSCode](#vscode)
    - [Jupyter](#jupyter)
    - [Jupyter VSCode Extension](#jupyter-vscode-extension)
    - [Docker](#docker)
    - [RabbitMQ](#rabbitmq)
    - [InfluxDB](#influxdb)
  - [Course Organization and Activities Index](#course-organization-and-activities-index)
  - [Repository Maintenance](#repository-maintenance)
  - [Frequently Asked Questions](#frequently-asked-questions)
    - [Example question](#example-question)

## Questions and Issues

If you encounter any problem, or have any questions, follow the steps:
1. Consult the [Frequently Asked Questions](#frequently-asked-questions).
2. Check if there are closed or open [issues](https://github.com/clagms/IncubatorDTCourse/issues)
3. Open an issue.
4. Contact your instructor/TA:
   1. For Aarhus, this is [Claudio](mailto:claudio.gomes@ece.au.dk)    2. For Polytechnique, this is [Bentley](mailto:bentley.oakes@polymtl) and/or [Roozbeh](mailto:roozbeh.aghili@polymtl.ca).

## Pre-Requisites

We assume the reader is somewhat familiar with the following tools. Tutorials are provided below, but we recommend the reader to search the web for the latest information:
1. Git
2. Python
3. Jupyter
4. VSCode
5. Docker
6. RabbitMQ
7. InfluxDB

### Git

Git is a version control system that tracks changes to projects in discrete 'commits'. In these notebooks, we will use Git to automatically pull in the latest version of some required incubator files such as datasets.

**Installation:**
1. Depending on your platform, you may have to install the git binary, and then a git graphical user interface.
2. The git binary can be obtained here, for your platform: https://git-scm.com/
3. The git user interface can be found here: https://git-scm.com/downloads/guis
   1. For windows, we recommend:
      1. https://git-scm.com/downloads/guis
   2. For mac, we recommend: 
      1. https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop
   3. For Linux, we recommend:
      1. https://github.com/sourcegit-scm/sourcegit

**Tutorial:** https://github.com/git-guides

### Python

We will use Python as the main programming language for creating the DT, due to its wide usage, versatility, and excellent library support.

**Installation:** 
1. Use [Python 3.11](https://www.python.org/) as minimum version. We recommend to install the latest python version, and revert to the suggested version if you face problems.
2. Install the python dependencies declared in the [requirements.txt](requirements.txt) file. Run `pip install -r requirements.txt`

**Tutorial:** 
1. https://docs.python.org/3.11/tutorial/index.html
2. Learn about virtual environments and the pip package manager to install python packages: https://docs.python.org/3.11/tutorial/venv.html

### VSCode

VSCode is an IDE (Integrated Development Environment), which is another way of saying 'code editor'. VSCode is optional, as there are many IDEs, but is recommended for running Python and Jupyter notebooks and for reading Markdown files.

**Installation:** 
1. https://code.visualstudio.com/docs/setup/setup-overview
2. Install the extensions:
   1. [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   2. [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) - Running and visualizing Jupyter notebooks
   3. [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) - Visualizing the markdown documentation

**Tutorial:** https://code.visualstudio.com/docs/introvideos/basics

### Jupyter

**Installation:** 
1. Install Jupyter notebook following instructions from: https://jupyter.org/install

**Tutorial:** 
1. Skim https://docs.jupyter.org/en/latest/
2. Learn about the Jupyter notebook, which is the interface we recommend for editing jupyter notebooks: https://jupyter-notebook.readthedocs.io/en/latest/

### Jupyter VSCode Extension

**Installation:** 
1. https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

**Tutorial:** 
1. Read the documentation in https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
2. If the extension is installed, you should be able to open the notebooks in this repository using VSCode, and interact with them.

### Docker

Docker is a set of software products that can "wrap" an application, together with its dependencies, into a "container". This means that applications in Docker containers can be more easily shared between different users on different platforms. Docker is heavily used within these modules to simplify tool setup.

**Installation:** https://www.docker.com/products/docker-desktop/

**Tutorial:**
1. Start on the materials under [0-Pre-requisites](0-Pre-requisites)
2. Complement them with https://docker-curriculum.com/

### RabbitMQ

RabbitMQ is a 'message broker', which means that it is software for routing messages. RabbitMQ can operate using different message protocols, and using queues and reliable messaging patterns, can enable messaging across devices and architectures. RabbitMQ is used throughout these modules for routing messages.

**Installation:** Not needed, since we will configure and run a RabbitMQ server using Docker.

**Tutorial:** 
1. Start on the materials under [0-Pre-requisites](0-Pre-requisites)
1. Complement them with the python tutorials in https://www.rabbitmq.com/tutorials 

### InfluxDB

InfluxDB is an open-source time-series database, which means that it stores data points and an associated time. It is used throughout these modules to capture and query system data.

**Installation:** Not needed, since we will configure and run an InfluxDB server using docker.

**Tutorial:** 
1. Start on the materials under [0-Pre-requisites](0-Pre-requisites)
2. Complement them with https://docs.influxdata.com/influxdb/v2/get-started/

## Course Organization and Activities Index

The course is organized in different folders, to be followed in their alphanumerical order.
Each folder contains one or more Jupyter notebooks that you should run and go carefully over.

## Repository Maintenance

1. Ensure that documentation links are not broken. 
   1. Use for example, [markdown-link-check](https://github.com/tcort/markdown-link-check) to check all md files for broken links:
      ```powershell
      Get-ChildItem -Include *.md -Recurse | Foreach {markdown-link-check --config .\markdown_link_check_config.json $_.fullname}
      ```
   2. If relevant, regenerate the [Table of Contents](#contents), either by hand or (recommended) using [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) or some other utility.
2. Run notebooks and check that there are no errors:
   ```powershell
    run_tests.ps1
   ```

## Frequently Asked Questions

### Example question


