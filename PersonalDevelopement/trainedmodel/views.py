# views.py

import openai
import spacy
from django.shortcuts import render

# Initialize OpenAI API client with your API key

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

def chat(request):
    return render(request, "chat.html")

def get_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        processed_input = process_input(user_input)
        response = generate_response(processed_input)
        return render(request, 'response.html', {'response': response})
    return render(request, 'chat.html')

def process_input(user_input):
    # Tokenize and tag user input using spaCy
    doc = nlp(user_input)
    # Extract nouns and proper nouns from the input
    nouns = [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']]
    # Concatenate the extracted words into a single string
    processed_input = " ".join(nouns)
    return processed_input

def generate_response(user_input):
    # Use processed user input as prompt for ChatGPT
    prompt = user_input
    
    # Generate response using ChatGPT
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Choose the appropriate ChatGPT model
        prompt=prompt,
        max_tokens=5
    )
    
    return response.choices[0].text.strip()
