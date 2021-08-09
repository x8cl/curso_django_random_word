from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def home(request):
    request.session["contador"] = 0
    return redirect("/random_word")

def random_word(request):
    r_word = get_random_string(length=14)

    context = {
        "word":r_word
    }
    request.session["contador"] += 1
    return render(request, "index.html", context)


