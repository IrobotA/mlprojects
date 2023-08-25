#common focntionalities project is going to use

import os  
import sys 
import dill #c'est quoi dill

import numpy as np 
import pandas as np 

from src.exception import CustomException

def save_object(file_path,obj): #sauvegarder objet
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok = True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)