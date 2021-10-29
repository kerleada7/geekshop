from django.urls import path

from .views import LoginListView, Logout, RegisterListView, ProfileFormView, verify

app_name = 'users'

urlpatterns = [
    path('login/', LoginListView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('verify/<str:email>/<str:activation_key>/', verify, name='verify'),
]