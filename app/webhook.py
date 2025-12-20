from app.pipeline.orchestrator import run_pipeline

def handle_webhook(payload):
    return run_pipeline(payload)
