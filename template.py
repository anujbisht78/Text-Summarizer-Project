# FOR WITTING ALL THE LOGIC

import os
from pathlib import Path
import logging

# Setting the logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# defining the base directory for the project
project_name = "Text_Summarizer"
list_of_files = [
    ".github/workflows/.gitkeep",   # beacuse we want to keep the .github directory even if it's empty 
    f"src/{project_name}/__init__.py",   # to make the src directory a package --> __init__.py file is used to mark a directory as a Python package4
    f"src/{project_name}/components/__init__.py",   # to make the components directory a package   
    f"src/{project_name}/utils/__init__.py",   # to make the utils directory a package
    f"src/{project_name}/utils/common.py",   # common utility functions
    f"src/{project_name}/logging/__init__.py",   # to make the logging directory a package
    f"src/{project_name}/config/__init__.py",   # to make the config directory a package
    f"src/{project_name}/config/configuration.py",   # configuration file for the project
    f"src/{project_name}/pipeline/__init__.py",   # to make the pipeline directory a package
    f"src/{project_name}/entity/__init__.py",   # to make the entity directory a package
    f"src/{project_name}/constants/__init__.py",   # to make the constants directory a package
    "config/config.yaml",   # configuration file for the project
    "dvc.yaml",   # dvc file for data version control
    "params.yaml",   # parameters file for the project
    "app.py",   # main application file
    "main.py",   # main entry point for the application
    "Dockerfile",   # Dockerfile for containerization 
    "requirements.txt",   # file listing the project dependencies
    "setup.py",  # setup file for packaging the project
    "research/trials.ipynb"   # Jupyter notebook for research and experimentation
]


# Looping through the list of files and creating them if they don't exist
for filepath in list_of_files:

    filepath = Path(filepath)   # creating a Path object for the file path

    # splitting the file path into directory and filename
    filedir, filename = os.path.split(filepath)   

    # checking if the directory exists, if not create it
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)   # creating the directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for the file: {filename}")   # logging the directory creation

    # checking if the file exists, if not create it
    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0): # checking if the file doesnt exist or is empty
        with open(filepath, "w") as f: 
            pass   # creating an empty file
        logging.info(f"Creating empty file: {filename}")   # logging the file creation

    else:
        logging.info(f"{filename} already exists")   # logging that the file already exists

        