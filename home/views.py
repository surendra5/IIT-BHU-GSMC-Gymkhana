from django.shortcuts import render, get_object_or_404
from .models import GameDetails, PostHolders, MainPostHolders
from django.http import HttpResponseRedirect, HttpResponse
from .forms import GymkhanaForm


def index(request):
    all_games = GameDetails.objects.all()
    main_posts = MainPostHolders.objects.all()
    context = {'all_games': all_games, 'main_posts': main_posts}
    return render(request, 'home/index.html', context)


def GymkhanaFormCreate(request):
    if request.method == 'POST':
        # to pull last filled details
        form = GymkhanaForm(request.POST)
        # cleaned form after submit
        # form = GymkhanaForm()
        if form.is_valid():
            form.save()
            form = GymkhanaForm()
    else:
        form = GymkhanaForm()
    data = {'form': form}
    return render(request, 'home/eventform.html', data)



def gamer(request, page_name):
    all_games = GameDetails.objects.all()
    game = GameDetails.objects.get(game_title=page_name)
    all_posts = GameDetails.objects.get(game_title=page_name).postholders_set.all()
    sam = 'home/' + page_name + '.html'
    context = {'all_posts': all_posts, 'game': game, 'all_games': all_games}
    return render(request, sam, context)
