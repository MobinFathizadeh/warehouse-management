from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginView, LogoutView,UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = [
    path('auth/login/', LoginView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('',include(router.urls)),
]