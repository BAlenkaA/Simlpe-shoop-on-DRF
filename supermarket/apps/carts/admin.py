from django.contrib import admin

from .models import ShoppigCart


@admin.register(ShoppigCart)
class ShoppigCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'amount')
    list_filter = ('user',)
