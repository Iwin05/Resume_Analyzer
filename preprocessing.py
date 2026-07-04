import re
import spacy

# load spaCy model
nlp = spacy.load("en_core_web_sm")


def clean_text(text):
    """
    Basic cleaning:
    - lowercase
    - remove extra spaces
    - remove unwanted symbols
    """
    
    text = text.lower()
    
    # remove extra whitespace (newline, tabs)
    text = re.sub(r'\s+', ' ', text)
    
    # keep only useful characters
    text = re.sub(r'[^a-zA-Z0-9\s\.\,\-\+]', '', text)
    
    return text.strip()


def preprocess_text(text):
    """
    Full preprocessing:
    cleaning + lemmatization + stopword removal
    """
    
    text = clean_text(text)
    
    doc = nlp(text)
    
    processed_tokens = []
    
    for token in doc:
        if not token.is_stop and not token.is_punct:
            processed_tokens.append(token.lemma_)
    
    return " ".join(processed_tokens)