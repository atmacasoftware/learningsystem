from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework import *
from rest_framework.views import APIView
from .models import Teacher
from .serializer import TeacherSerializer
from rest_framework import generics

#class TeacherList(APIView):
#    def get(self,request):
#        teachers = Teacher.objects.all()
#        serializer = TeacherSerializer(teachers, many=True)
#        return Response(serializer.data)

class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
