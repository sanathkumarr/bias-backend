from collections import Counter
import re

def clean_text(text):
    """
    Cleans and preprocesses text for better comparison.
    """
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

def compute_bias_score(original_text, alternative_texts):
    """Compares original text with alternatives to compute bias."""
    biased_words = set()
    bias_score = 0
    
    for alt_text in alternative_texts:
        words = set(alt_text.split())
        original_words = set(original_text.split())
        bias_words_in_text = original_words - words
        biased_words.update(bias_words_in_text)
    
    if len(original_text.split()) > 0:
        bias_score = round((len(biased_words) / len(original_text.split())) * 100, 2)
    
    return bias_score, biased_words