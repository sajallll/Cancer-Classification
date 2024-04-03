from cnnClassifier import logger
from cnnClassifier.pipeline.stafe_01_data_ingestion import DataIngestion

STAGE_NAME ="Data Ingestion Stage"

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e