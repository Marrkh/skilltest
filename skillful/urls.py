from django.contrib import admin
from django.urls import path
from .serializer import *
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),

    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('subjects/', SubjectsView.as_view(), name='subjects'),
    path('tests/', TestsBySubjectView.as_view(), name='tests'),

    # path('subjects/tests/', TokenVerifyView.as_view(), name='subject-tests'),


]
