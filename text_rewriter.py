import difflib

def replace_biased_content(original_text, biased_words, alternative_texts):
    """Replaces biased content with neutral wording based on alternatives."""
    rewritten_text = original_text
    
    for word in biased_words:
        for alt_text in alternative_texts:
            if word in alt_text:
                rewritten_text = rewritten_text.replace(word, alt_text.split()[alt_text.split().index(word)])
                break
    
    return rewritten_text