from django.urls import path

from authapp.views import RegisterView, Logout, ProfileFormView, LoginLogView

app_name = 'authapp'
urlpatterns = [
    path('login/', LoginLogView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('verify/<str:email>/<str:activate_key>/', RegisterView.verify, name='verify')
]
