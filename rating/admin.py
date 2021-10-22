from django.contrib import admin
from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'poster',
        'comment',
        'rating',
        'product_id',
        'updated',
        'created',
    )

admin.site.register(Rating, RatingAdmin)

