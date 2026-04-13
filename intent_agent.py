from base_agent import AIWorker

def run_intent_phase(business_ask):
    intent_specialist = AIWorker(
        name="Intent-Analyst",
        role="Principal Business Analyst / Product Owner",
        model_type="gpt-4o-mini" # Cost-effective for logic extraction
    )
    
    prd_output = intent_specialist.execute(
        task_input=business_ask,
        context="Analyze requirements and define core KPIs for a $1M budget project."
    )
    return prd_output

if __name__ == "__main__":
    test_ask = "We need a system to automate food benefit optimization on Azure."
    print(run_intent_phase(test_ask))
