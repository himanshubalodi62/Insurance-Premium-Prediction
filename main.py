from insurance.logger import logging
from insurance.exception import InsuranceException
from insurance.utils import get_collection_as_dataframe
import sys,os
from insurance.entity import config_entity
from insurance.components.data_ingestion import DataIngestion
from insurance.components.data_validation import DataValidation
from insurance.components.data_transformation import DataTransformation
from insurance.components.model_trainer import ModelTrainer
from insurance.components.model_evaluation import ModelEvaluation
from insurance.components.model_pusher import ModelPusher
from insurance.pipeline.training_pipeline import start_training_pipeline
from insurance.pipeline.batch_prediction import start_batch_prediction

input_file_path="/config/workspace/insurance_main_dataset.csv"
print(__name__)
if __name__=="__main__":
     try:
          #start_training_pipeline()
          output_file = start_batch_prediction(input_file_path=input_file_path)
          print(output_file)         
     except Exception as e:
          print(e)
