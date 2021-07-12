from django.shortcuts import render
from .models import Notes
# Create your views here.
def createNote(request):
	if request.method == "POST":
		title = request.POST["title"]
		date = request.POST["date"]
		body = request.POST["body"]
		Notes.objects.create(title=title,date=date,body=body)
		data = Notes.objects.all()
		return render(request,"myApp/view-note.html",{"data":data})
	return render(request,"myApp/create-note.html",{})

def viewNote(request):
	data = Notes.objects.all()
	return render(request,"myApp/view-note.html",{"data":data})

def deleteNote(request,Id):
	Notes.objects.filter(id=Id).delete()
	data = Notes.objects.all()
	return render(request,"myApp/view-note.html",{"data":data})

def update(request,Id):
	data = Notes.objects.get(id=Id)
	print(data.date)
	if request.method == "POST":
		title = request.POST["title"]
		date = request.POST["date"]
		body = request.POST["body"]
		Notes.objects.filter(id=Id).update(title=title,date=date,body=body)
		data = Notes.objects.all()
		return render(request,"myApp/view-note.html",{"data":data})
	return render(request,"myApp/edit-note.html",{"data":data})