from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students = [
    {"name": "Pritam", "age": 22, "id": 1}
    ]
    return HttpResponse(students)