import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):

    doc = nlp(text)
    keywords = set()

    stop_phrases = {
        "experience","ability","knowledge","skills",
        "work","project","team","year"
    }

    for chunk in doc.noun_chunks:
        phrase = chunk.text.strip().lower()

        #filter
        if (len(phrase) > 2 and phrase not in stop_phrases and len(phrase.split()) <= 3):
            keywords.add(phrase)
    
    for token in doc:
        word = token.text.lower()

        if(token.pos_ in ["NOUN","PROPN"] and len(word) > 2):
            keywords.add(word)
    
    return list(keywords)
    
    

