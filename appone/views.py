from django.shortcuts import render, redirect, HttpResponse
from .forms import PrepForm, ReviewForm
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key = openai_key)

# Create your views here.
def home(request):
    return render(request, "home.html")

def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            saved_form = form.save()
            subject = saved_form.subject


            # Process subject with OpenAI API
            user_message = "Give me 5 key points on " + subject + ". Return the key points only."

            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an insturctor, skilled in helping students review different courses and topics for exams."},
                    {"role": "user", "content": user_message}
                ]
            )

            print(completion.choices[0].message)

            return redirect("review") # Return to the same page rn
    else:
        form = ReviewForm()

    return render(request, "review.html", {"form" : form})

def prep(request):
    if request.method == "POST":
        form = PrepForm(request.POST)
        if form.is_valid():
            saved_form = form.save()
            subject = saved_form.subject

            # Process subject with OpenAI API
            user_message = "Give me 5 practice exam quetions on " + subject + ". Return questions and answers only."

            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an insturctor, skilled in helping students review different courses and topics for exams."},
                    {"role": "user", "content": user_message}
                ]
            )

            print(completion.choices[0].message)


            return redirect("prep") # Return to the same page rn
    else:
        form = PrepForm()
        
    return render(request, "prep.html", {"form" : form})

