from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

challenge_list = {
    "January": "Learn a new language for 30 minutes every day",
    "February": "Write a short story or poem each week",
    "March": "Do 20 minutes of yoga or meditation daily",
    "April": "Try a new recipe every weekend",
    "May": "Take a nature walk twice a week",
    "June": "Learn to play a new musical instrument",
    "July": "Read a book outside your usual genre",
    "August": "Start a daily journaling habit",
    "September": "Volunteer for a cause you care about",
    "October": "Explore a new hiking trail every weekend",
    "November": "Practice gratitude by keeping a gratitude journal",
    "December": None
}



# Create your views here.

def index(request):
    months = list(challenge_list.keys())


    
    response = render_to_string("challenges/challenge.html")
    return render(request,"challenges/index.html",{
        "months":months 
    })

def monthly_challenges_bynum(request,month):
    months = list(challenge_list.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Index do not exists")
    
    redirect_month = months[month-1]
    redirect_path = reverse("monthly_challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path) 

def monthly_challenges(request, month):
    try:
        text = challenge_list[month]
        
        return render(request,"challenges/challenge.html",{
            "text":text,
            "month_name":month,
        })
    except:
        return HttpResponseNotFound(month+" do not exist")
     