# Purpose

This project is a calculator for getting regions of interest from a excel table from an
experiment.

# Installation

## Windows
1. Install [Python 3.7](https://www.python.org/downloads/release/python-370/)
2. Install [Git](https://git-scm.com/download/win)
3. Install [pip](https://pip.pypa.io/en/stable/installing/)
4. Install [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)

## Linux
1. Install Python 3.7
2. Install Git
3. Install pip
4. Install virtualenv

# Install requirements

```bash
pip install -r requirements.txt
```

# Run the project

```bash
python main.py
```

# For easy execution in windows

```ps1
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

This will make it possible to execute the ps1 script.
Afterwards run it with 

```ps1
.\setup_env.ps1
```

Afterwards run the script with
```ps1
python -m src.main
```