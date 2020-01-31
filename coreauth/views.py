from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, UserSerializerWithToken, UserSerializerForRegister
from .models import User

class handle_user(APIView):
    # permission_classes = [permissions.IsAdminUser]
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        user_id = request.GET['pk']
        user_info = User.objects.get(pk=int(user_id))
        serializer = UserSerializer(user_info)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        user_id = request.data['pk']
        User.objects.get(pk=int(user_id)).delete()

        return Response({"success": True}, status=status.HTTP_202_ACCEPTED)

    def put(self, request, *args, **kwargs):
        user_id = request.data['pk']
        user_info = User.objects.get(pk=int(user_id))
        if 'first_name' in request.data:
            user_info.first_name = request.data['first_name']
        if 'last_name' in request.data:
            user_info.last_name = request.data['last_name']
        if 'company_name' in request.data:
            user_info.company_name = request.data['last_name']
        if 'user_role' in request.data:
            user_info.user_role = request.data['user_role']

        user_info.save()

        serializer = UserSerializer(user_info)

        return Response(serializer.data, status=status.HTTP_200_OK)

class new_user(APIView):
    """
    Create a new user.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerForRegister(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)           
            