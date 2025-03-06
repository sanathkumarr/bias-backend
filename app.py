from flask import Flask, request, jsonify
from scraper import scrape_alternative_sources
from bias_detector import compute_bias_score
from text_rewriter import replace_biased_content
from highlighter import highlight_changes
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.get_json()
    original_text = data.get('text', '').strip()
    if not original_text:
        return jsonify({"error": "No text provided"}), 400
    
    try:
        # Scrape alternative sources
        alternative_texts = scrape_alternative_sources(original_text)
        if not alternative_texts:
            return jsonify({"error": "Could not retrieve alternative sources"}), 500
        
        # Compute bias score and detect biased words
        bias_score, biased_words = compute_bias_score(original_text, alternative_texts)
        
        # Rewrite text with neutral wording
        rewritten_text = replace_biased_content(original_text, biased_words, alternative_texts)
        
        # Highlight changes
        highlighted_text = highlight_changes(original_text, rewritten_text)
        
        return jsonify({
            "original_text": original_text,
            "rewritten_text": rewritten_text,
            "highlighted_text": highlighted_text,
            "bias_score": bias_score,
            "biased_words": list(biased_words)
        })
    except Exception as e:
        logging.error(f"Error processing text: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
