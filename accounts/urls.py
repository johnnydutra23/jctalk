from django.urls import path
from accounts.views import SigningView, SignUpView, UserView

urlpatterns = [
    path('signin', SigningView.as_view()),
    path('signup', SignUpView.as_view()),
    path('me', UserView.as_view())
]