from django.http import HttpResponse 
from django.shortcuts import render
from news.models import Adduser
from django.views import View
from . import api
import json
import requests, smtplib 

def index(request):
    return render(request,'index.html',{"title":"TOPNEWS"})

def signup(request):
    return render(request,'signup.html',{"title":"TOPNEWS"})



def signup_view(request):

    if (request.POST):
        
        signup_data = request.POST.dict()
        
        
        
        
       # if signup_data["Password"] == signup_data["CPassword"]
        #    del signup_data["CPassword"]
        del signup_data["csrfmiddlewaretoken"] 
        try:
            Adduser.objects.get(Email= signup_data["Email"])   
        except Adduser.DoesNotExist as e:
            

            new_user = Adduser.objects.create( **signup_data )
            new_user.save()
            #for sending email after subcription
            s = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
            s.login("preexam668@gmail.com", "exam@9988")
            message = "Thanks for subscribing TOPNEWS"
            s.sendmail("preexam668@gmail.com", signup_data["Email"], message)
            s.quit()

            error = "Thanks for subscribing TOPNEWS"
            return render(request,"signin.html",{"title": "TOPNEWS","error":error })
        else:
            error = "User already exits"
            return render(request,"signup.html",{"error":error,"title":"TOPNEWS"})
        
        #else:
        #error = "password doesnot match..please try again"
        #return render(request,"signup.html",{"error":error,"title":"TOPNEWS"})
    else:
        error = " Your Method is not post!!Try Again"
        return render(request,"signup.html",{"error":error,"title":"TOPNEWS"})

def news_blog(request):
    data1 = api.news
    
    d = []
    for i in data1:
        news_data = {
            "author": i[0],
            "title" : i[1],
            "content": i[2],
            "url" : i[3],
            "description" : i[4],
        }
        d.append(news_data)
    return render(request, "index.html",{"data":d,"title":"TOPNEWS"})

def weather(request,city=None):

    if (request.POST):
        
        city = request.POST.dict()
        print(city)
        CITY = city["city"]
        url = "https://openweathermap.org/data/2.5/weather?q{}uk&appid=b6907d289e10d714a6e88b30761fae22".format(CITY)
        JSONContent = requests.get(url).json()
        j_resp = json.dumps(JSONContent,indent = 4)
        content = json.loads(j_resp)
        print(content)

        weather_data = {
        "weather_status" : content["weather"][0]["description"],
        "temp_status" : content["main"]["temp"],
        "wind_status" : content["wind"]["speed"],
        "humidity" : content["main"]["humidity"],    }  
        return render(request,"weather.html",{"weather": weather_data,"title":"WEATHER","city": CITY})



    


                
                

          

          
