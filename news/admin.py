from django.contrib import admin

from news.models import News, Comment

admin.site.register(Comment)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','create_at', 'changed_at', 'published_at', 'published']
    list_filter = ['title','create_at', 'published_at']