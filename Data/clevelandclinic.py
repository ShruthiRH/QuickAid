import json
import os
from bs4 import BeautifulSoup
import requests

scenario_name = 'Stroke'
symptom_description =[]
cause_description=[]
detailed_steps =[]
url = "https://my.clevelandclinic.org/health/diseases/5601-stroke#symptoms-and-causes"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
symptoms_causes_section = soup.find("div", {"id": "symptoms-and-causes"})
if symptoms_causes_section:
    symptoms_list = symptoms_causes_section.find("ul")
    if symptoms_list:
        #print("Symptoms of stroke:")
        for symptom in symptoms_list.find_all("li"):
            symptom_description.append(symptom.text.strip())

print("Symptoms of stroke:")
for symptom in symptom_description:
    print(symptom)

# Extract detailed emergency steps
treatment_section = soup.find("div", {"id": "management-and-treatment"})
if treatment_section:
    steps_list = treatment_section.find_all("li")
    for index, step in enumerate(steps_list, start=1):
        detailed_steps.append({
            "step_number": index,
            "step_description": step.text.strip()
        })

# Prepare data for JSON
data = {
    "scenarios": [
        {
            "scenario_id": 2,
            "scenario_name": scenario_name,
            "symptoms & causes": symptom_description,
            "detailed_steps": detailed_steps
        }
    ]
}

with open('medicaldataset.json','a') as json_file:
    json.dump(data,json_file, indent=4)

print(f"JSON file saved in: {os.getcwd()}")










