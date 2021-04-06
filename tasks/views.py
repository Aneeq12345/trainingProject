from django.shortcuts import render
from .models import tasks
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.db import connection
from django.db.models import Q,F
# Create your views here.

class tasksList(APIView):
  
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, pk,format=None):
        
        taskList = tasks.objects.filter(user=pk)
        serializer = TaskSerializer(taskList, many=True)
        return Response(serializer.data)

    def post(self, request, pk,format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response([serializer.data], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class taskDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return tasks.objects.get(pk=pk)
        except tasks.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response([serializer.data], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
