#WITH PHRASE MATCHER

import json
from flask import Flask, request, jsonify, send_from_directory
import spacy
from spacy.matcher import PhraseMatcher
from flask_cors import CORS

app = Flask(__name__, static_folder='')
CORS(app)

# Load the medical dataset
with open('medicaldataset.json') as f:
    data = json.load(f)

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Initialize PhraseMatcher
matcher = PhraseMatcher(nlp.vocab, attr='LOWER')

# Add symptoms to the matcher
symptoms_list = []
for scenario in data['scenarios']:
    symptoms_list.extend(scenario.get('symptoms & causes', []))

patterns = [nlp(symptom) for symptom in symptoms_list]
matcher.add("SYMPTOMS", patterns)

def extract_keywords(text):
    doc = nlp(text)
    matches = matcher(doc)
    keywords = [doc[start:end].text for match_id, start, end in matches]
    return keywords

def match_scenario(keywords):
    best_match = None
    max_matches = 0
    for scenario in data['scenarios']:
        symptoms = scenario.get('symptoms & causes', [])
        matches = len(set(keywords) & set(symptoms))
        if matches > max_matches:
            max_matches = matches
            best_match = scenario
    return best_match

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message', '')
    keywords = extract_keywords(user_input)
    scenario = match_scenario(keywords)
    if scenario:
        detailed_steps = [step['step_description'] for step in scenario['detailed_steps']]
        response = {
            'introduction': scenario['introduction'],
            'detailed_steps': detailed_steps
        }
    else:
        response = {
            'message': "I'm sorry, I couldn't identify the symptoms. Please seek immediate medical attention."
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)