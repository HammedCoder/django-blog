from .views import SignUpView
from django.urls import path


urlpatterns = [
    path('', SignUpView.as_view(), name="signup")
]