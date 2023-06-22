from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
# Create your views here.

class StudentViewset(viewsets.ViewSet):
    def list(self,request):
        data=Student.objects.all()
        serializer=StudentSerializer(data,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=StudentSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created sucessfully'})
        else:
            return Response({'msg':'data not created'})