from rest_framework.response import Response
from rest_framework.views import APIView
from ..models.user_model import CustomUser
from ..serializers import CustomUserSerializer


class UserView(APIView):
    def get(self,request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users,many=True)
        return Response(serializer.data)