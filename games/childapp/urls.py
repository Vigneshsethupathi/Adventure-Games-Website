from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),

    #--------------game part-----------------------------------------------
    path('goosebumbs/', views.goosebumbs, name='goosebumbs'),
    path('xmen/', views.xmen, name='xmen'),
    path('hill_climber/', views.hill_climber, name='hill_climber'),
    path('gears_of_war/', views.gears_of_war, name='gears_of_war'),
    path('hulk/', views.hulk, name='hulk'),
    path('iron/', views.iron, name='iron'),
    path('nfs/', views.nfs, name='nfs'),
    path('Resident_Evil/', views.Resident_Evil, name='Resident_Evil'),
    path('GTA_4/', views.xmen, name='GTA_4'),
    path(' delta_force/', views.delta_force, name='delta_force'),
    path('Tomb_Raider/', views.Tomb_Raider, name='Tomb_Raider'),
    path('Prince_of_Persia/', views.iron, name='Prince_of_Persia'),
    path('Evil_Dead/', views.Evil_Dead, name='Evil_Dead'),
    path('Assassins_Creed/', views.Assasion_Creed, name='Assasion_Creed'),
    path('cod4/', views.cod4, name='cod4'),
    path('dragon/', views.dragon, name='dragon'),
    path('GTA_vice_city/', views.GTA_vice_city, name='GTA_vice_city'),
    path('GTA_IV/', views.GTA_IV, name='GTA_IV'),
    path('prince_of_persia_II/', views.prince_of_persia_II, name='prince_of_persia_II'),
    path('Far_cry_3/', views.Far_cry_3, name='Far_cry_3'),
    path('Alien_Shooter/', views.Alien_Shooter, name='Alien_Shooter'),

    # secound home------------
    path('page2/', views.home2, name='home2'),

    # third home------------
    path('page3/', views.home3, name='home3'),

    #nav links---------------------
    path('Action/', views.Action, name='Action'),
    path('adventure/', views.adventure, name='adventure'),
    path('arcade', views.arcade, name='arcade'),
    path('Fighting', views.Fighting, name='Fighting'),
    path('GTA_GAMES', views.GTA_GAMES, name='GTA_GAMES'),
    path('Horror', views.Horror, name='Horror'),
    path('no_games', views.no_games, name='no_games'),
    path('Puzzle', views.Puzzle, name='Puzzle'),
    path('Racing', views.Racing, name='Racing'),
    path('shooting', views.shooting, name='shooting'),
    path('Simulation', views.Simulation, name='Simulation'),
    path('about', views.about, name='about'),
    #------login
    path('login', views.login, name='login'),

]