def calculate_score(match_result):

    matched = match_result["matched"]
    missing = match_result["missing"]

    total = len(matched) + len(missing)

    if total == 0:
        return 0
    
    score = (len(matched) / total) * 100

    return round(score,2)

def score_label(score):

    if score >= 80:
        return "Strong Match"
    elif score >= 60:
        return "Moderate Match"
    else:
        return "what the hell is this?"