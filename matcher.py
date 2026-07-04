#additional improvements : synnonyms and embedding 

def match_keywords(resume_keywords, jd_keywords):
    
    resume_set = set(resume_keywords)
    jd_set = set(jd_keywords)

    matched = resume_set.intersection(jd_set)
    missing = jd_set - resume_set

    if len(jd_set) == 0:
        score = 0
    else:
        score = (len(matched) / len(jd_set)) * 100
    
    return {
        "matched":list(matched),
        "missing":list(missing),
        "score":round(score,2)
    }
