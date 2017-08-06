from django.contrib import admin
from .models import GameDetails, GymkhanaFormModel, PostHolders, MainPostHolders  #GamePage,
from .forms import GymkhanaForm
admin.site.register(GameDetails)
#admin.site.register(GamePage)
#admin.site.register(GymkhanaForm)
admin.site.register(GymkhanaFormModel)
admin.site.register(PostHolders)
admin.site.register(MainPostHolders)