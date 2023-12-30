from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
from django.shortcuts import render
import requests
import os


def index(request):
    context={
        "variable":"RJ_POLICE",
        "variable2":"RJ_POLICE"
    }
    return render(request,'index.html',context)
    # return Http Response ("This Is HOME PAGE")

def support(request):
    context={
        "variable":"RJ_POLICE",
        "variable2":"HE iS GOOD"
    }
    return render(request,'support.html',context)

def neutralizer(request):
    context={
        "variable":"MRJ_POLICE",
        "variable2":"HE iS GOOD"
    }
    return render(request,'neutralizer.html',context)

def index(request):
    context={
        "variable":"RJ_POLICE",
        "variable2":"HE iS GOOD"
    }
    return render(request,'index.html',context)
    # return Http Response ("This Is HOME PAGE")

def support(request):
    context={
        "variable":"RJ_POLICE",
        "variable2":"HE iS GOOD"
    }
    return render(request,'support.html',context)


def input_form(request):
    return render(request, 'try1.html')

# Load the trained model from a file
#clf = joblib.load('static/model3.joblib')

import google.generativeai as genai

genai.configure(api_key="AIzaSyDlv95Vd8NtDI3LVIlq_C0WWk2y8eUbxpM")
model = genai.GenerativeModel('gemini-pro')



def fact(user_input):
    
    data= user_input

    prompt="The following is a conversation with an AI Assistand for AI Legal Decision assistant for India specially for Rajasthan. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nOUTPUT: I am an AI Legal Decision System created by Team : Hackstormers. How can I help you today?\nHuman: {} ?".format(data)
    responseAI = model.generate_content(prompt)
    return responseAI.text

def check_string(input_string):
    # Split the input string into a list of words
    words = input_string.lower().split(' ')
    
    # Check if any of the forbidden words are in the list
    if 'no,' in words or 'no' in words or 'no' in words or 'sorry,' in words:
        return False
    else:
        return True


# Create a function to process the user input and return the prediction
def predict_article(request):
    if request.method == 'POST':
        # Get the user's input from the form
        user_input = request.POST.get('article')

        # # Convert the user's input to numerical features using HashingVectorizer
        # vectorizer = HashingVectorizer(stop_words='english', n_features=2**10)
        # user_input_vector = vectorizer.transform([user_input])

        # # Predict the label of the user's input using the trained model
        # prediction = clf.predict(user_input_vector)[0]
         #API
        responseme=fact(user_input)
        Ans=responseme

    
        # Return the prediction to the user on a new page
        if (True ) :
            print(responseme)            
            knowledge1=fact(user_input)
            print(knowledge1)
            return render(request, 'prediction.html', {'article':Ans})
        
    else:
        return HttpResponse('Invalid request method.')