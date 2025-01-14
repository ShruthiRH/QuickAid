import json
from flask import Flask, request, jsonify, send_from_directory
import spacy
from spacy.matcher import PhraseMatcher
from flask_cors import CORS
import speech_recognition as sr
import pyttsx3

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

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        return user_input
    except sr.UnknownValueError:
        return "I couldn't understand the audio."
    except sr.RequestError:
        return "Request error."

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message', '')
    if user_input == "voice":
        user_input = recognize_speech()
    
    keywords = extract_keywords(user_input)
    scenario = match_scenario(keywords)
    if scenario:
        detailed_steps = [step['step_description'] for step in scenario['detailed_steps']]
        response = {
            'introduction': scenario['introduction'],
            'detailed_steps': detailed_steps
        }
        speak(scenario['introduction'] + ". " + " ".join(detailed_steps))
    else:
        response = {
            'message': "I'm sorry, I couldn't identify the symptoms. Please seek immediate medical attention."
        }
        speak(response['message'])
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
