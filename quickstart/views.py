from django.contrib.auth.models import User, Group
from .models import Code
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer, CodeSerializer
import sys, traceback, subprocess

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

class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        mes = self.request.query_params.get('message')
        codes = []
        compile = ''
        proc = open("./tmp.py", "w")
        proc.write(mes)
        proc.close()
        try:
            process = subprocess.Popen(["python", ".\\tmp.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            compile = process.communicate()[0]
        except:
            # print(e)
            compile=traceback.format_exc()
        code = Code(message=compile)
        codes.append(code)
        return codes