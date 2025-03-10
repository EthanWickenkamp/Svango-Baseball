from django.contrib import admin
from .models import Item
from .models import Team, Game, Player, GameStat, AtBat

admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(GameStat)
admin.site.register(AtBat)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

