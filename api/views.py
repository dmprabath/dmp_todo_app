from tasks.models import Tasks
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Tasks.objects.all().order_by('-id')
    serializers = TaskSerializer(tasks, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Tasks.objects.get(id=pk)
    serializers = TaskSerializer(tasks, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def taskCreate(request):
    serializers = TaskSerializer(data= request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Tasks.objects.get(id=pk)
    serializers = TaskSerializer(instance=tasks, data= request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Tasks.objects.get(id=pk)
    tasks.delete()
    return Response("Deleted")
