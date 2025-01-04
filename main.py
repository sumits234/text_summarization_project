from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger


def execute_stage(stage_name, pipeline_class):
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        pipeline = pipeline_class()
        pipeline.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


# Stages Execution
STAGE_NAME = "Data Ingestion stage"
execute_stage(STAGE_NAME, DataIngestionTrainingPipeline)

STAGE_NAME = "Data Validation stage"
execute_stage(STAGE_NAME, DataValidationTrainingPipeline)

STAGE_NAME = "Data Transformation stage"
execute_stage(STAGE_NAME, DataTransformationTrainingPipeline)

STAGE_NAME = "Model Trainer stage"
logger.info(f"*******************")
execute_stage(STAGE_NAME, ModelTrainerTrainingPipeline)

STAGE_NAME = "Model Evaluation stage"
logger.info(f"*******************")
execute_stage(STAGE_NAME, ModelEvaluationTrainingPipeline)
