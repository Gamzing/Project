from django.shortcuts import render
from transformers import pipeline

# Load the GPT-3 model for text generation
text_generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

def home(request):
    return render(request, 'home.html')

def get_response(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = generate_response(user_input)
        return render(request, 'response.html', {'response': response})
    return render(request, 'home.html')

def generate_response(user_input):
    # Generate response using GPT-3
    response = text_generator(user_input, max_length=50, do_sample=False)[0]['generated_text']
    return response

