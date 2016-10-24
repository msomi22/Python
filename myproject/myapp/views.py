from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def hello(request):
	today = datetime.datetime.now().date()
	daysOfWeek = ['Mon','Tue','Wed','Thurs','Fri','Sat','Sun']
	return render(request,"hello.html",{"today_date":today,"days_of_week":daysOfWeek}) 

def morning(reques):
	message = """ <h2> Hello, i am Django , the Python framework </h2> """
	return HttpResponse(message) 

def reminder(request):
	msg = "Hello Mwenda!"
	return HttpResponse(msg)