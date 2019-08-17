from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),#회원가입
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/delete/', views.profile_delete, name='delete'),
    path('user_history', views.user, name="history"),

    path('password_change/', views.MyPasswordChangeView.as_view(), name='password_change'),

 #   path('login/url/', views.RequestLoginViaUrlView.as_view(), name='request_login_via_url'),
#    path('login/<uidb64>/<token>/', views.login_via_url, name='login_via_url'),

    path('password_change/', views.MyPasswordChangeView.as_view(), name='password_change'),


   # path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
  #  path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

