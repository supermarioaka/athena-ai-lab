def analyze_problem(problem_text, mode):
    problem_lower = problem_text.lower()

    if "markov" in problem_lower:
        problem_type = "Stochastic Processes / Markov Chain"
        suggested_approach = "Identify states, transition probabilities, communicating classes, and stationary behavior."
    elif "regression" in problem_lower:
        problem_type = "Statistics / Regression"
        suggested_approach = "Identify dependent variable, independent variables, assumptions, and coefficient interpretation."
    elif (
        "maximum" in problem_lower
        or "minimum" in problem_lower
        or "optimize" in problem_lower
    ):
        problem_type = "Optimization"
        suggested_approach = "Identify objective function, constraints, feasible region, and optimality conditions."
    elif "probability" in problem_lower:
        problem_type = "Probability"
        suggested_approach = (
            "Identify random variables, events, assumptions, and probability rules."
        )
    else:
        problem_type = mode
        suggested_approach = "Break the problem into known information, unknowns, assumptions, and a logical solution path."

    return {
        "problem_type": problem_type,
        "given_information": "Known quantities, definitions, assumptions, and mathematical objects.",
        "unknown_goal": "What we need to find, prove, estimate, explain, or decide.",
        "suggested_approach": suggested_approach,
    }
