from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teams/', views.team_list, name='team_list'),
    path('teams/create_team/', views.team_create, name='team_create'),
    path('teams/update/<int:team_id>/', views.team_update, name='team_update'),
    path('teams/delete/<int:team_id>/', views.team_delete, name='team_delete'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    #path('teams/<int:team_id>/players/', views.player_list, name='player_list'),
    path('teams/<int:team_id>/players/create/', views.player_create, name='player_create'),
    path('teams/<int:team_id>/players/update/<int:player_id>/', views.player_update, name='player_update'),
    path('teams/<int:team_id>/players/delete/<int:player_id>/', views.player_delete, name='player_delete'),

    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

]