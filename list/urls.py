from django.urls import path

from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users',views.UserView.as_view(),name = 'users list'),

    path('tasks', views.TaskView.as_view(), name='tasks list'),
    path('tasks/edit/<int:pk>', views.TaskView.as_view(), name='edit task'),

    path('chats', views.ChatView.as_view(), name='chats')
]