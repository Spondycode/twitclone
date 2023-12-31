from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('profile_list/', views.profile_list, name="profile-list"),
    path('profile/<int:pk>', views.profile, name="profile"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('register', views.register, name="register"),
]
