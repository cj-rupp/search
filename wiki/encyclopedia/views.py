from django.shortcuts import render
from html import unescape

from . import util
from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def post(request, title):

    converter = Markdown()

    marked = util.get_entry(title)
    text = converter.convert(marked)

    if marked != None:
        return render(request, "encyclopedia/page.html", {
            "title": title,
            "text": text
        })

