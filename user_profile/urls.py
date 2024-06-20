from django.urls import path
from .import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('delete_user_purchased/<int:id>/', views.DeleteProfilePost.as_view(), name='delete_user_purchased'),
    path('change_profile/', views.EditProfile.as_view(), name='change_profile'),
]
