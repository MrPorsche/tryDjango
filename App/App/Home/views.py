from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):

    Candidates = [
        {"name": "Ilyas Sayyed", "age": 27, "geo": "Nigdi"},
        {"name": "Usman Bagwan", "age": 22, "geo": "Sawantwadi"},
        {"name": "Anzal Sayyed", "age": 17, "geo": "Kondhwa"},
        {"name": "Aslam Shaikh", "age": 32, "geo": "Karad"},
        {"name": "Sufiyan Shaikh", "age": 15, "geo": "Dehuroad"},
        {"name": "Javed Saleem", "age": 10, "geo": "Pimpri"},
    ]

    Veggies = ["Tomato", "Potato", "Ladyfinger", "Cocumber", "Pumpkin"]

    return render(request, "Home.html", context= {"Candidates": Candidates, "Vegitables": Veggies})

def Success(request):
    return render(request, "Success.html")