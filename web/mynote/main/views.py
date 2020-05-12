from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddNewNote
from .models import Note
from django.views import generic
from flask import request
from django.utils import timezone

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'note_list'
    def get_queryset(self):
        return Note.objects.filter(user = self.request.user)

def add_note(response):
    if response.method == "POST":
        form = AddNewNote(response.POST)
        if form.is_valid():
            c = form.cleaned_data["category"]
            t = form.cleaned_data["tag"]
            l = form.cleaned_data["link"]
            con = form.cleaned_data["content"]
            md = timezone.now()
            n = Note(category=c, tag=t, link = l, modify_date=md, content=con)
            n.save() 
            response.user.note.add(n)
            return redirect('../index') 
    else:
        form = AddNewNote()
    return render(response, "main/add_note.html", {"form": form})

def home(response):
    return render(response, "main/home.html", {})
