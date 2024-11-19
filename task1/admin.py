from django.contrib import admin
from .models import Buyer, Game


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'balance',)
    search_fields = ('name', 'balance')
    list_filter = ('balance', 'name',)
    list_per_page = 10


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title', 'description',)
