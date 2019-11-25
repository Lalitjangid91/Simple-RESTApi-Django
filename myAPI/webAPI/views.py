from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializers

class StudentList(APIView):
    def get(self,request):
        students1=Student.objects.all()
        serlizer=StudentSerializers(students1,many=True)
        return Response(serlizer.data)
    def post(self):
        pas