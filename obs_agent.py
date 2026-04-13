from base_agent import AIWorker

def run_observation_phase(deployed_system):
    observer = AIWorker(
        name="SRE-Monitor",
        role="Site Reliability & QA Engineer",
        model_type="gpt-4o-mini"
    )
    
    health_check = observer.execute(
        task_input=deployed_system,
        context="Define App Insights alerts and automated unit tests for the deployment."
    )
    return health_check
