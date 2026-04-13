from base_agent import AIWorker

def run_planning_phase(final_design):
    planner = AIWorker(
        name="Sprint-Master",
        role="Technical Project Manager / Scrum Master",
        model_type="gemini-1.5-flash"
    )
    
    roadmap = planner.execute(
        task_input=final_design,
        context="Break this design into a 4-week sprint plan with clear tickets."
    )
    return roadmap
