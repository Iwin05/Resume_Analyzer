def generate_feedback(match_result,score):

    matched = match_result["matched"]
    missing = match_result["missing"]

    feedback = []
    strength = []
    suggestions = []
    inspire = []

    #feedback for the missing skills
    if missing:
        feedback.append(
            f"Your resume is missing important skills like {', '.join(missing[:5])}."
        )
    else:
        feedback.append("Your Resume covers most of the required skills")

    #stengths taken from the feedback
    if matched:
        strength.append(
            f"you have relevant skill such as {', '.join(matched[:5])}."
        )
    
    #suggestions depending on the score
    if score < 50:
        suggestions.append(
            "Your resume has low alignment with the job.Focus on adding core required skills."
        )
    elif score < 75:
        suggestions.append(
            "Your resume shows moderate alignment.Improve by adding missing skills and refining your projects."
        )
    else:
        suggestions.append(
            "Your resume is well aligned.Consider improving clarity and adding advanced skills."
        )

    #inspiration - idk why
    inspire.append(
        "Don't give up even if your score is low. focus on the goal ahead."
    )

    return {
        "feedback":feedback,
        "strength":strength,
        "suggestions":suggestions,
        "inspire":inspire
    }