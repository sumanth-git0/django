from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Chat
from ..serializers import ChatSerializer
from ..utils import chatcompletion


class ChatView(APIView):
    def get(self,request):
        chat = Chat.objects.filter(user=request.user.id)
        serializer = ChatSerializer(chat,many=True)
        return Response(serializer.data)

    def post(self,request):
        request.data['user'] = request.user.id
        request.data['sender'] = 'user'
        chat = Chat.objects.filter(user = request.user.id)
        print(chat)
        print(request.data)
        messages = []
        for message in chat:
            messages.append({
                "role": message.sender,
                "content": message.text
            })
        serializer = ChatSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            messages.append({
                "role": serializer.data['sender'],
                "content": serializer.data['text']
            })
            response = chatcompletion(messages)
            Chat.objects.create(user=request.user, text=response, sender='system')
            return Response(serializer.data)
        return Response(serializer.errors)
