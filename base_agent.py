import os

class AIWorker:
    def __init__(self, name, role, model_type):
        self.name = name
        self.role = role
        self.model_type = model_type

    def execute(self, task_input, context=""):
        print(f"\n>>> [AGENT: {self.name}] starting work...")
        
        # This is where you'd integrate with your company's Copilot / OpenAI / Gemini API
        # For your demo, we simulate the output flow
        prompt = f"""
        ACT AS: {self.role}
        CONTEXT: {context}
        TASK: {task_input}
        
        DELIVERABLE: Provide a professional English technical document or code.
        """
        
        # Simulation of the API response
        result = f"--- FINAL DELIVERABLE FROM {self.name} ({self.model_type}) ---\n"
        result += f"High-quality output for: {task_input[:30]}...\n"
        return result
