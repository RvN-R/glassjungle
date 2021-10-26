from django.contrib import admin
from .models import Forum

class ForumAdmin(admin.ModelAdmin):
    list_display = (
        'poster',
        'title',
        'comment',
        'updated',
        'created',
        'image',
    )


admin.site.register(Forum, ForumAdmin)
