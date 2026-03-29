import os
import yaml
from src.datascience import logger
import json
import joblib
from pathlib import Path
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (str): The file path to the YAML file.
    Returns:
        ConfigBox: A ConfigBox object containing the contents of the YAML file.
    Raises:
        FileNotFoundError: If the specified YAML file does not exist.
        yaml.YAMLError: If there is an error parsing the YAML file.
    """
    if not os.path.exists(path_to_yaml):
        raise FileNotFoundError(f"The specified YAML file does not exist: {path_to_yaml}")
    
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML file: {e}")
        raise
    except BoxValueError as e:
        logger.error(f"Error creating ConfigBox: {e}")
        raise
    
@ensure_annotations
def create_directories(path_to_directories: list):
    """
    Creates directories specified in the list if they do not already exist.

    Args:
        path_to_directories (list): A list of directory paths to be created.
    Returns:

    Raises:
        OSError: If there is an error creating any of the directories.
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            logger.info(f"Directory created or already exists: {path}")
        except OSError as e:
            logger.error(f"Error creating directory {path}: {e}")
            raise
        
@ensure_annotations
def save_json(path: str, data: dict):
    """
    Saves a dictionary as a JSON file at the specified path.

    Args:
        path (str): The file path where the JSON file will be saved.
        data (dict): The dictionary to be saved as JSON.
    Returns:

    Raises:
        OSError: If there is an error writing to the file.
        TypeError: If the data provided is not serializable to JSON.
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"Data successfully saved to JSON file: {path}")
    except OSError as e:
        logger.error(f"Error writing to file {path}: {e}")
        raise
    except TypeError as e:
        logger.error(f"Data provided is not serializable to JSON: {e}")
        raise
    
@ensure_annotations
def load_json(path: str) -> dict:
    """
    Loads a JSON file and returns its contents as a dictionary.

    Args:
        path (str): The file path to the JSON file.
    Returns:
        dict: A dictionary containing the contents of the JSON file.
    Raises:

        FileNotFoundError: If the specified JSON file does not exist.
        json.JSONDecodeError: If there is an error parsing the JSON file.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The specified JSON file does not exist: {path}")
    
    try:
        with open(path
, 'r') as json_file:
            data = json.load(json_file)
            logger.info(f"Data successfully loaded from JSON file: {path}")
            return data
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON file: {e}")
        raise
    except OSError as e:
        logger.error(f"Error reading file {path}: {e}")
        raise
    
@ensure_annotations
def save_bin(path: str, model: Any):
    """
    Saves a machine learning model to the specified path using joblib.

    Args:
        path (str): The file path where the model will be saved.
        model (Any): The machine learning model to be saved.
    Returns:

    Raises:
        OSError: If there is an error writing to the file.
        TypeError: If the model provided is not serializable by joblib.
    """
    try:
        joblib.dump(model, path)
        logger.info(f"Model successfully saved to: {path}")
    except OSError as e:
        logger.error(f"Error writing to file {path}: {e}")
        raise
    except TypeError as e:
        logger.error(f"Model provided is not serializable by joblib: {e}")
        raise
    
@ensure_annotations
def load_bin(path: str) -> Any:
    """
    Loads a machine learning model from the specified path using joblib.

    Args:
        path (str): The file path to the model file.
    Returns:
        Any: The machine learning model loaded from the file.
    Raises:

        FileNotFoundError: If the specified model file does not exist.
        OSError: If there is an error reading the file.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The specified model file does not exist: {path}")
    
    try:
        model = joblib.load(path)
        logger.info(f"Model successfully loaded from: {path}")
        return model
    except OSError as e:
        logger.error(f"Error reading file {path}: {e}")
        raise