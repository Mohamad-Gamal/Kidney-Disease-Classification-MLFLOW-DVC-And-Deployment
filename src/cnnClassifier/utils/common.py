import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    '''✅ 1. read_yaml(path_to_yaml: Path) -> ConfigBox
        ✔️ Purpose:
        Reads a YAML configuration file and converts it into a ConfigBox object so you can access keys using dot notation (e.g., config.model.name instead of config['model']['name']).

        🧠 Explanation:
        python
            @ensure_annotations
            def read_yaml(path_to_yaml: Path) -> ConfigBox:
        Enforces that the input must be a Path and output will be a ConfigBox.

        Uses ensure_annotations to check types at runtime.

        python
            with open(path_to_yaml) as yaml_file:
                content = yaml.safe_load(yaml_file)
        Loads YAML contents into a Python dictionary.

        python
            return ConfigBox(content)
        Converts that dictionary into a ConfigBox for dot-style access.

        python
            except BoxValueError:
                raise ValueError("yaml file is empty")
        Custom error if the file exists but has no data.

        python
            except Exception as e:
                raise e
        Catches any other exception and re-raises it.

        🔄 Use Case:
        python
            config = read_yaml(Path("config.yaml"))
            print(config.model.name)
    '''
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data
    🔹 Purpose:
        Load data from a .json file and return it as 
        a ConfigBox (which supports dot notation like config.param).

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
    🔹 Purpose:
        Save any Python object (model, data, etc.) 
        as a binary file using joblib — very common for saving ML models.

    🧠 Why joblib?
        It’s faster and more efficient than pickle for 
        large numpy arrays or scikit-learn models.

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
        🔹 Purpose:
        Get the size of a file in kilobytes (KB),
        rounded to the nearest whole number.

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    '''🔹 Purpose:
        Convert a Base64-encoded string (e.g. from an API input) 
        back into an image and save it as a file.'''

    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    '''🔹 Purpose:
            Read an image file and return its Base64-encoded version, 
            often used when you want to send
            an image over an API or save it in text format (like JSON).'''
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

