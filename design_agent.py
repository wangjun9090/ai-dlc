from base_agent import AIWorker

def run_design_phase(prd_document):
    # The Cross-Check Logic
    gemini_architect = AIWorker("Architect-Gemini", "Cloud Solutions Architect", "gemini-1.5-pro")
    claude_architect = AIWorker("Architect-Claude", "Lead Systems Designer", "claude-3-opus")
    
    print("--- Running Cross-Check Design ---")
    design_v1 = gemini_architect.execute(prd_document, "Focus on Azure Native integration.")
    design_v2 = claude_architect.execute(prd_document, "Focus on scalability and security.")
    
    # In your demo, you can show both and say you picked the best
    return design_v1, design_v2

if __name__ == "__main__":
    print(run_design_phase("Sample PRD Requirements"))
