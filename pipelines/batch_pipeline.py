from jobs.ingestion import run as ingestion
from jobs.transformation import run as transformation
from jobs.aggregation import run as aggregation

def run_pipeline():
    raw_path = ingestion()
    processed_path = transformation(raw_path)
    aggregation(processed_path)