from django.shortcuts import render
from django.http import HttpResponseRedirect

def mainpage(request):
	return render(request, "main/main.html")

def submit(request):
	if request.method == "POST":
		info = request.POST
		return HttpResponseRedirect("/wait", {"info":info})

def wait(request):
	return render(request, "main/wait.html")
