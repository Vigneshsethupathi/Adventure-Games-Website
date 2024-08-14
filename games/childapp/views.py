from django.shortcuts import render
from django.template  import loader
from django.http import HttpResponse

def home(request):
    template = loader.get_template(('index.html'))
    return HttpResponse(template.render())

#page's-------

#secound home---------------
def home2(request):
    template =loader.get_template(('homepage/home3.html'))
    return HttpResponse(template.render())
#third home---------------
def home3(request):
    template =loader.get_template(('homepage/home2.html'))
    return HttpResponse(template.render())

#------------------------------------gamepart--------------------------------------------------------
def goosebumbs(request):
    template = loader.get_template(('gamepart/goosebumbs.html'))
    return HttpResponse(template.render())
def xmen(request):
    template = loader.get_template(('gamepart/xmen.html'))
    return HttpResponse(template.render())
def hill_climber(request):
    template = loader.get_template(('gamepart/hill climber.html'))
    return HttpResponse(template.render())
def gears_of_war(request):
    template = loader.get_template(('gamepart/gears_of_war.html'))
    return HttpResponse(template.render())
def hulk(request):
    template = loader.get_template(('gamepart/hulk.html'))
    return HttpResponse(template.render())
def iron(request):
    template = loader.get_template(('gamepart/iron.html'))
    return HttpResponse(template.render())
def nfs(request):
    template = loader.get_template(('gamepart/nfs.html'))
    return HttpResponse(template.render())
def Resident_Evil(request):
    template = loader.get_template(('gamepart/Resident Evil-4.html'))
    return HttpResponse(template.render())
def GTA_4(request):
    template = loader.get_template(('gamepart/GTA 4.html'))
    return HttpResponse(template.render())
def delta_force(request):
    template = loader.get_template(('gamepart/Delta force(black haven).html'))
    return HttpResponse(template.render())
def Tomb_Raider(request):
    template = loader.get_template(('gamepart/Tomb Raider.html'))
    return HttpResponse(template.render())
def Prince_of_Persia(request):
    template = loader.get_template(('gamepart/Prince-of-Persia.html'))
    return HttpResponse(template.render())
def Evil_Dead(request):
    template = loader.get_template(('gamepart/Evil Dead.html'))
    return HttpResponse(template.render())
def Assasion_Creed(request):
    template = loader.get_template(('gamepart/Assasion Creed.html'))
    return HttpResponse(template.render())
def cod4(request):
    template = loader.get_template(('gamepart/Call Of Duty-4.html'))
    return HttpResponse(template.render())
def dragon(request):
    template = loader.get_template(('gamepart/Dragon Age II.html'))
    return HttpResponse(template.render())
def GTA_vice_city(request):
    template = loader.get_template(('gamepart/GTA vice city.html'))
    return HttpResponse(template.render())
def GTA_IV(request):
    template = loader.get_template(('gamepart/GTA IV.html'))
    return HttpResponse(template.render())
def prince_of_persia_II(request):
    template = loader.get_template(('gamepart/Prince-of-Persia II.html'))
    return HttpResponse(template.render())
def Far_cry_3(request):
    template = loader.get_template(('gamepart/Far Cry 3.html'))
    return HttpResponse(template.render())
def Alien_Shooter(request):
    template = loader.get_template(('gamepart/Alien Shooter.html'))
    return HttpResponse(template.render())

#---------------nav link--------------

def Action(request):
    template = loader.get_template(('nav list/Action.html'))
    return HttpResponse(template.render())
def adventure(request):
    template = loader.get_template(('nav list/adventure.html'))
    return HttpResponse(template.render())
def arcade(request):
    template = loader.get_template(('nav list/arcade.html'))
    return HttpResponse(template.render())
def Fighting(request):
    template = loader.get_template(('nav list/Fighting.html'))
    return HttpResponse(template.render())
def GTA_GAMES(request):
    template = loader.get_template(('nav list/GTA_games.html'))
    return HttpResponse(template.render())
def Horror(request):
    template = loader.get_template(('nav list/Horror.html'))
    return HttpResponse(template.render())
def no_games(request):
    template = loader.get_template(('nav list/no games.html'))
    return HttpResponse(template.render())
def Puzzle(request):
    template = loader.get_template(('nav list/Puzzle.html'))
    return HttpResponse(template.render())
def Racing(request):
    template = loader.get_template(('nav list/Racing.html'))
    return HttpResponse(template.render())
def shooting(request):
    template = loader.get_template(('nav list/shooting.html'))
    return HttpResponse(template.render())

def Simulation(request):
    template = loader.get_template(('nav list/Simulation.html'))
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template(('nav list/about.html'))
    return HttpResponse(template.render())


#-------login-----------
def login(request):
    template = loader.get_template(('login/login.html'))
    return HttpResponse(template.render())