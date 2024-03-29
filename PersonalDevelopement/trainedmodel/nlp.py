import requests
import spacy
from django.shortcuts import render

# Load the English language model
nlp = spacy.load('en_core_web_sm')

def recommend_content(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        recommendations = get_recommendations(user_input)
        return render(request, 'recommendations.html', {'recommendations': recommendations})
    return render(request, 'index.html')

def get_recommendations(user_input):
    # Perform NLP analysis on user input
    doc = nlp(user_input)
    
    # Extract keywords or entities from the user input
    keywords = [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']]
    
    # Make a GET request to the API endpoint with keywords
    api_url = f'sk-EgB0l3U7i9kBwLwesvjpT3BlbkFJn1JjQSXarXAkErDn0Npyrecommendations?keywords={",".join(keywords)}'
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        recommendations = response.json()
        return recommendations
    else:
        # Handle errors gracefully
        return []
