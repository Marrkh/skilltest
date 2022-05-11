from rest_framework import generics, permissions, mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializer import *
from .models import Subject
from rest_framework.permissions import AllowAny, BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.generics import ListAPIView
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend


class RegisterView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "User Created Successfully.",
        })


class SubjectsView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TestsBySubjectView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TestSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TestFilter

    def get_queryset(self):
        tests = Test.objects.all()
        return tests

