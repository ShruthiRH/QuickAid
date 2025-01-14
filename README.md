# Medical Chatbot

This project is a **Medical Chatbot** designed to assist users in identifying symptoms of medical conditions and providing step-by-step guidance on what to do in case of emergencies. It combines **Natural Language Processing (NLP)**, **speech recognition**, **text-to-speech (TTS)**, and a simple **Flask web server** to deliver an interactive experience.



## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Features
1. **Symptom Matching:** Detects symptoms and matches them to predefined scenarios using NLP and a medical dataset.
2. **Voice Input:** Accepts voice input using speech recognition for hands-free interaction.
3. **Text-to-Speech:** Responds with voice feedback for improved accessibility.
4. **Step-by-Step Guidance:** Provides detailed instructions for handling medical emergencies.
5. **User-Friendly Interface:** Includes a simple HTML front-end for input and output display.
6. **Cross-Origin Support:** Enabled with Flask-CORS for easy integration with external applications.

---

## Technologies Used
- **Backend:**
  - Flask
  - Flask-CORS
  - Spacy (NLP)
  - SpeechRecognition
  - pyttsx3 (Text-to-Speech)
- **Frontend:**
  - HTML, CSS, JavaScript
- **Data Storage:**
  - JSON file for storing medical scenarios
- **NLP Model:**
  - Spacy's `en_core_web_sm`

---

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Internet connection for downloading dependencies

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/medical-chatbot.git
   cd medical-chatbot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the Spacy language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open a web browser and navigate to `http://127.0.0.1:5000`.

---

## Usage
1. Open the chatbot interface in your browser.
2. Enter your symptoms in the text box or use the "Record Voice" button for voice input.
3. Receive:
   - A brief introduction to the potential condition.
   - Step-by-step guidance on how to manage the situation.
   - Voice feedback with the same instructions.

---

## How It Works

1. **Data Matching:**  
   - A JSON file (`medicaldataset.json`) contains medical scenarios with symptoms and corresponding instructions.
   - Symptoms are matched using Spacy's `PhraseMatcher`.

2. **Voice Input and Output:**
   - **Input:** SpeechRecognition captures and converts speech to text.
   - **Output:** pyttsx3 provides text-to-speech functionality for responses.

3. **Symptom Extraction:**
   - User input is processed using NLP to extract keywords.
   - Keywords are compared to the dataset to identify the closest matching scenario.

4. **Response Generation:**
   - If a match is found, the chatbot retrieves the scenario introduction and detailed steps.
   - If no match is found, it advises seeking immediate medical attention.

---

## Project Structure


medical-chatbot/
│
├── app.py                   # Flask application
├── medicaldataset.json      # Medical scenarios dataset
├── static/
│   ├── styles.css           # CSS for the front-end
├── templates/
│   └── index2.html          # Front-end HTML template
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation


---

## API Endpoints

### `/`
- **Method:** GET
- **Description:** Serves the front-end HTML page.

### `/chatbot`
- **Method:** POST
- **Description:** Accepts a message (text or voice) from the user and responds with:
  - The identified medical condition.
  - Step-by-step instructions to handle it.

## Future Enhancements
1. Database Integration: Replace the JSON dataset with a database for scalability.
2. Multi-Language Support: Add support for multiple languages in NLP and TTS.
3. Mobile App: Create a mobile-friendly version using frameworks like Flutter.
4. Expanded Dataset: Include more medical scenarios and symptoms.
5. Machine Learning Integration: Enhance symptom matching with ML models for better accuracy.


