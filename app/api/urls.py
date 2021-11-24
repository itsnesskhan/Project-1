from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    ApiRoots,
    UserRegisterApiView,
    UserUpdateApiView,
)



urlpatterns = [
    path('', ApiRoots.as_view()),
    path('user/', UserRegisterApiView.as_view(), name = 'user-list'),
    path('user/<int:pk>', UserUpdateApiView.as_view(), name = 'user-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('rest_framework.urls'))


]
