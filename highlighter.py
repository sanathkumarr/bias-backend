import difflib

def highlight_changes(original_text, rewritten_text):
    """Highlights the differences between original and rewritten text."""
    diff = difflib.ndiff(original_text.split(), rewritten_text.split())
    highlighted_text = []

    for word in diff:
        if word.startswith("- "):
            highlighted_text.append(f"<del>{word[2:]}</del>")  # Mark removed words
        elif word.startswith("+ "):
            highlighted_text.append(f"<ins>{word[2:]}</ins>")  # Mark added words
        else:
            highlighted_text.append(word[2:])

    return " ".join(highlighted_text)