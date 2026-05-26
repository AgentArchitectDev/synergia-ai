class PromptOptimizer:

    def optimize(self, prompt):

        optimized = f"""
Act as a senior AI business engineer.

Generate:

- professional response
- structured output
- strategic analysis
- implementation steps
- automation ideas

USER REQUEST:
{prompt}
"""

        return optimized


prompt_optimizer = PromptOptimizer()
