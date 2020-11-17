from django.shortcuts import render
from django import forms
import re

from . import util
from markdown2 import Markdown

from random import choice

class SearchForm(forms.Form):
    q = forms.CharField(label="search")

class EditForm(forms.Form):
    title = forms.CharField(label="save")
    content = forms.CharField(label="save")

converter = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def post(request, title):
    marked = util.get_entry(title)

    if marked != None:
        text = converter.convert(marked)
        return render(request, "encyclopedia/page.html", {
            "title": title,
            "text": text
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })

def random(request):
    entries = util.list_entries()
    selected = choice(entries)
    marked = util.get_entry(selected)
    return render(request, "encyclopedia/page.html", {
        "title": selected,
        "text": converter.convert(marked)
    })

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            pattern = form.cleaned_data["q"]
            text = util.get_entry(pattern)
            if text != None:
                return render(request, "encyclopedia/page.html", {
                    "title": pattern,
                    "text": converter.convert(text) 
                })
            else:
                matcher = re.compile(pattern)
                entries = util.list_entries()
                found = []
                for entry in entries:
                    if(matcher.search(entry)) :
                        found.append(entry)
                if len(found) > 0:
                    return render(request, "encyclopedia/result.html", {
                        "matches": found
                    })
                else:
                    return render(request, "encyclopedia/error.html", {
                        "title": pattern
                    })
        else:
            return render(request, "encyclopedia/error.html", {
                "title": form.errors
            })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": request.method       
        })

def edit(request,title):
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "text": util.get_entry(title)
    })

def newPage(request):
    return render(request, "encyclopedia/blank.html")

def save(request):
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title,content)
            return render(request, "encyclopedia/page.html", {
                "title": title,
                "text": converter.convert(content)
            })
        else:
            return render(request, "encyclopedia/edit.html", {
                "title": title,
                "text": form.errors
            })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": request.method
        })
        

