import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.dat_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainingPipeline:
    def __init__(self) -> None:
        pass
    def iniciate_training_pipeline(self):
        logging.info('Started')
        obj=DataIngestion()
        train_data_path,test_data_path=obj.initiate_data_ingestion()
        data_transformation = DataTransformation()
        train_arr,test_arr,_=data_transformation.initaite_data_transformation(train_data_path,test_data_path)
        model_trainer=ModelTrainer()
        model_trainer.initate_model_training(train_arr,test_arr)