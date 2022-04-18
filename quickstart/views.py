from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer, RepoSerializer
from main.models import RepoInformation
from rest_framework import generics

from django.shortcuts import redirect

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class QueryViewSet(viewsets.ModelViewSet):

    queryset = RepoInformation.objects.all()
    serializer_class = RepoSerializer
    permission_classes = [permissions.IsAuthenticated]


def scrapy_redirect(request):
    return redirect('https://github.com/scrapy', permanent=True)

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


