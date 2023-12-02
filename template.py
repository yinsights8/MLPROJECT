import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "Mlproject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/Components/__init__.py",
    f"src/{project_name}/Components/data_ingestion.py",
    f"src/{project_name}/Components/data_transformation.py",
    f"src/{project_name}/Components/model_trainer.py",
    f"src/{project_name}/Components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile.py",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    # print(filepath)
    filedir, filename = os.path.split(filepath)
    # print(filedir, filename)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Created directory : {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info("{filename} already exists")