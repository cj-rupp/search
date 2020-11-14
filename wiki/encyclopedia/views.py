from django.shortcuts import render
from django import forms
import re

from . import util
from markdown2 import Markdown

from random import choice

class SearchForm(forms.Form):
    q = forms.CharField(label="search")

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
            "title": "method"        
        })




