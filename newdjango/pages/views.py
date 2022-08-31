from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request,*args,**kwargs):
	my_content = {
		"my_text" : "This is about us",
		"my_number" : 123,
		"my_list" : [1,2,3]
	}

	return render(request,"home.html",my_content) #string of html code