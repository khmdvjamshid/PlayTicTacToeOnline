from django.contrib import admin
from . models import GameState, WinState, UserSymbol
# Register your models here.
admin.site.register(GameState)

admin.site.register(WinState)

admin.site.register(UserSymbol)