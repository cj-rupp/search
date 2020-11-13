from django.shortcuts import render
from html import unescape

from . import util
from markdown2 import Markdown

from random import choice

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


