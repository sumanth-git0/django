from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.task_model import Task
from ..serializers import TaskSerializer


class TaskView(APIView):
    def get(self,request,pk=None):
        tasks = Task.objects.filter(user = request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self,request):
        request.data['user'] = request.user.id
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        # Update an existing task
        try:
            task = Task.objects.get(pk=pk,user=request.user)  # Ensure task belongs to the logged-in user
        except Task.DoesNotExist:
            return Response({'detail': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data, partial=True)  # Partial to allow partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk,user=request.user)
        except Task.DoesNotExist:
            return Response({'detail': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response({'detail': 'Task deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


