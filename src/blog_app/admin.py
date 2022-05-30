from django.contrib import admin
from blog_app.models import Article

from cms.admin.placeholderadmin import PlaceholderAdminMixin

# Register your models here.


class ArticleAdmin(PlaceholderAdminMixin,admin.ModelAdmin):
    pass

admin.site.register(Article,ArticleAdmin)
