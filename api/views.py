# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view (['GET','POST'])
# Create your views here.
def studentsView(request):
    #students = Student.objects.all()
    #students = queryset
    #here we are manually serializing the data
    #student_list = list(students.values())
    #by default JsonRespose think we are sending the dictonary
    #we have to serialize the data first. 
    #for sending the another type of data instead of the dict
    #we have to pass the safe parameter as false
    #return JsonResponse(student_list, safe=False)
    if request.method == 'GET':
        #Get all the data from the student table.
        students = Student.objects.all()
        
        #serialize the data
        #Many=> True is for the multiple students. 
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
