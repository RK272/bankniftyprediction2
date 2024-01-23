import os
from pathlib import Path

package_name="bankniftyPricePrediction"

list_of_files=[
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/cloud_storage/__init__.py",
    f"src/{package_name}/cloud_storage/s3_syncer.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_transformation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/data_access/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/ml/__init__.py",
    f"src/{package_name}/ml/metric/__init__.py",
    f"src/{package_name}/ml/metric/classification_metric.py",
    f"src/{package_name}/ml/model/__init__.py",
    f"src/{package_name}/ml/model/estimator.py",
    f"src/{package_name}/entity/artifact_entity.py",
    f"src/{package_name}/entity/config_entity.py",
    f"src/{package_name}/data_access/stock_data.py",
    f"src/{package_name}/configuration/__init__.py",
    f"src/{package_name}/configuration/mogo_db_connection.py",
    f"src/{package_name}/constant/__init__.py",
    f"src/{package_name}/constant/training_pipline/__init__.py",
    f"src/{package_name}/constant/application.py",
    f"src/{package_name}/constant/database.py",
    f"src/{package_name}/constant/env_variable.py",
    f"src/{package_name}/constant/s3_bucket.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/training_pipeline.py",
    f"src/{package_name}/pipelines/prediction_pipeline.py",
    f"src/{package_name}/logger.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/main_utils.py",
    "notebooks/research1.ipynb",
    "notebooks/research2.ipynb",
    "notebooks/research3.ipynb",
    "notebooks/research4.ipynb",
    "notebooks/research5.ipynb",
    "notebooks/research6.ipynb",
    "notebooks/data/.gitkeep",
    "requirements.txt",
    "setup.py",
    "init_setup.sh",
]


# here will create a directory

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    """ how exist_ok works:if "directory" already exists, 
    os.makedirs() will not raise an error, and it will do nothing. 
    If "my_directory" doesn't exist, it will create the directory.
    """
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")

# here will use the file handling


