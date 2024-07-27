from django.shortcuts import render, redirect, HttpResponse
from .forms import PrepForm, ReviewForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            saved_form = form.save()
            subject = saved_form.subject
            print(subject)
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
            return redirect("prep") # Return to the same page rn
    else:
        form = PrepForm()
        
    return render(request, "prep.html", {"form" : form})

