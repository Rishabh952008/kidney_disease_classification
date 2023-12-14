import os
from pathlib import Path
import logging

# logging string (why i need this logging string whenever you will be executing this file what are the activity
# actually this file will do this let say creating folder and all this kind of messages you will be able to see from
# terminal itself you will be able to log them from terminal instead of using print statement)
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

# i need to create some lsit of files and folders 
list_of_files = [
    ".github/workflows/.gitkeep", # i will create .github folder inside that i will be creating another folder workflows inside it file .gitkeep
    # if i folder is empty git will not consider it so added temporary .gitkeep file inside workflows folder
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config/yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
       os.makedirs(filedir, exist_ok=True)
       logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath))  or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")
    else:
        logging.info(f"{filename} is already exisiting ")
    