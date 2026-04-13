from base_agent import AIWorker

def run_deployment_phase(codebase):
    devops = AIWorker(
        name="DevOps-Engineer",
        role="Azure Cloud & CI/CD Expert",
        model_type="gemini-1.5-pro"
    )
    
    infra_code = devops.execute(
        task_input=codebase,
        context="Generate Terraform scripts and GitHub Action workflows for Azure deployment."
    )
    return infra_code
