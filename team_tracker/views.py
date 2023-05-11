from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Team, Player
from .forms import TeamForm, PlayerForm


    
@login_required
def home(request):
    teams = Team.objects.order_by('city')
    return render(request, 'home.html', {'teams': teams})

@login_required
def team_list(request):
    teams = Team.objects.all()
    show_links = False
    if teams.exists():
        show_links = True
    return render(request, 'team/team_list.html', {'teams': teams, 'show_links': show_links})

@login_required
def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    print(f"Team ID: {team.id}")  # Debug output
    players = team.players.all()
    print(f"player id: {players}")
    return render(request, 'team/team_detail.html', {'team': team, 'players': players})



@login_required
def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'team/team_create.html', {'form': form})

@login_required
def team_update(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_detail', team_id=team.id)
    else:
        form = TeamForm(instance=team)
    return render(request, 'team/team_update.html', {'form': form, 'team': team})


@login_required
def team_delete(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'team/team_delete.html', {'team': team})

#@login_required
#def player_list(request, team_id):
#    team = get_object_or_404(Team, id=team_id)
#    players = team.players.all()
#    return render(request, 'players/player_list.html', {'players': players, 'team': team})

@login_required
def player_create(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.team = team
            player.save()
            return redirect('team_detail', team_id=team.id)
    else:
        form = PlayerForm()
    return render(request, 'players/player_create.html', {'form': form, 'team': team})

@login_required
def player_update(request, team_id, player_id):
    team = get_object_or_404(Team, id=team_id)
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('team_detail', team_id=team.id)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'players/player_update.html', {'form': form, 'team': team})

@login_required
def player_delete(request, team_id, player_id):
    team = get_object_or_404(Team, id=team_id)
    player = get_object_or_404(Player, id=player_id)
    player.delete()
    return redirect('team_detail', team_id=team.id)