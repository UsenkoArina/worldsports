from django.contrib import admin
from . models import SportCategory, Article, Comment

admin.site.register(SportCategory)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    exclude = ('likes', 'saved_by',) # Remove the "likes" field from the admin page

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'created_at', 'text')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'article__article_title', 'text')


