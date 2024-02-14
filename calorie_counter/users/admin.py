from django.contrib import admin
from .models import User, Product, Dish, Recipe

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'birth_date',
                    'height', 'weight', 'gender', 'physical_activity', 'target')

    list_display_links = ('username', 'email')
    search_fields = ('birth_date', 'target')


admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Dish)
admin.site.register(Recipe)
