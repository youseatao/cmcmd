from django.shortcuts import render

def mainpage(request):
	return render(request, "main/main.html")
