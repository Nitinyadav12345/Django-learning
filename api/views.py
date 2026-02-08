from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

# Create your views here.
def studentsView(request):
    students = Student.objects.all()
    #students = queryset
    #here we are manually serializing the data
    student_list = list(students.values())
    #by default JsonRespose think we are sending the dictonary
    #we have to serialize the data first. 
    #for sending the another type of data instead of the dict
    #we have to pass the safe parameter as false
    return JsonResponse(student_list, safe=False)