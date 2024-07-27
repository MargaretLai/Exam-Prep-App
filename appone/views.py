from django.shortcuts import render, redirect, HttpResponse
from .forms import PrepForm, ReviewForm, EmailSignupForm
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

            # Render response to user
            key_points = completion.choices[0].message.content
            key_points = key_points.split("\n")

            return render(request, "review.html", {"form" : form, "key_points" : key_points})
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

            # Render response to user
            questions_and_answers = completion.choices[0].message.content
            questions_and_answers = questions_and_answers.split("\n")       
            questions = []
            answers = []
            for item in questions_and_answers:
                if "Question" in item:
                    questions.append(item)
                elif "Answer" in item:
                    answers.append(item)

            return render(request, "prep.html", {"form" : form, "questions" : questions, "answers" : answers})
    else:
        form = PrepForm()
        
    return render(request, "prep.html", {"form" : form})

def email_signup(request):
    if request.method == "POST":
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            pass
    else:
        form = EmailSignupForm() 

    return render(request, "email_signup.html", {"form": form})