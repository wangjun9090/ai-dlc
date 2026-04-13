from base_agent import AIWorker

def run_development_phase(sprint_tasks):
    developer = AIWorker(
        name="Lead-Dev",
        role="Senior Full-Stack AI Engineer",
        model_type="claude-3-opus" # Best for complex coding
    )
    
    codebase = developer.execute(
        task_input=sprint_tasks,
        context="Write production-ready Python and React code following SOLID principles."
    )
    return codebase
