
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ),
    path('signup/', views.RegistrationView.as_view(), name ="signup"),
    path('login/', views.SinginView.as_view(), name ="signin"),
    path('logout/', views.sign_out, name ="signout"),
    path('user-detail/', views.UserDetailView, name ="user-detail"),
    path('update/<int:id>', views.edit_data, name ="editdata"),
    path('delete/<int:id>', views.delete_data, name ="deletedata"),
    path('api/', include('app.api.urls')),
]
