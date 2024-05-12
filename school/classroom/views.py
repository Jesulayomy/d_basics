from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from classroom.serializers import (
    ClassroomSerializer,
    StudentSerializer,
    TeacherSerializer,
)
from classroom.models import (
    Classroom,
    Student,
    Teacher,
)


class StudentsView(APIView):
    def get(self, request):
        students = Student.objects.all()
        classroom = StudentSerializer(students, many=True)
        return Response(classroom.data, status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        student = StudentSerializer(data=data, partial=True)
        if student.is_valid():
            student.save()
            return Response(student.data)
        else:
            return Response({}, status.HTTP_400_BAD_REQUEST)


class StudentView(APIView):

    def get(self, request, id):
        student = Student.objects.get(pk=id)
        serialized = StudentSerializer(student)
        return Response(serialized.data, status.HTTP_200_OK)

    def put(self, request, id):
        student = Student.objects.get(pk=id)
        data = request.data
        serialized = StudentSerializer(student, data=data, partial=True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status.HTTP_202_ACCEPTED)

    def delete(self, request, id):
        # Wrap .get() calls in ter except for Model.DoesNotExist
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({}, status.HTTP_204_NO_CONTENT)


class TeachersView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
