from django.urls import include, path
from userapp import views, api_views as apv

urlpatterns = [
    path('', views.login),
    path('login/', views.login),
    path('signout/', views.signout),
    path('user-registration/', views.user_registration),
    path('base/', views.base),
    path('dashboard/', views.dashboard),
    path('user-profile/', views.user_profile),
    path('user-profile-update/<int:id>/', views.user_profile_update),
    path('<int:id>/delete-user/', views.user_delete),
    path('user-list/', views.user_list),

# API Url
    path('app-user-registration/', apv.user_registration),
    path('app-user-profile-update/', apv.user_profile_update),
    path('app-user-list/', apv.user_list),
    path('app-user-delete/', apv.user_delete),
    path('app-user-login/', apv.login),


   
   
]
