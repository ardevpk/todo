from django.contrib import admin
from app.models import Testing, NewsApi
# Register your models here.
class serviceReg(admin.ModelAdmin):
    list_display = ('User', 'Name', 'Title', 'Desc', 'date', 'time')


class newsReg(admin.ModelAdmin):
    list_display = ('News_title', 'News_author', 'News_desc', 'News_image')


admin.site.register(NewsApi, newsReg)


admin.site.register(Testing, serviceReg)
# admin.site.register(NewsApi)