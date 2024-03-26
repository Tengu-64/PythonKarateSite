from django.contrib import admin
from .models import *

class di(admin.ModelAdmin):
    list_display = ('id', 'name', 'translate')
    list_display_links = ('id', 'name', 'translate')
    search_fields = ('id', 'name', 'translate')

class blt(admin.ModelAdmin):
    list_display = ('kyu', 'color', 'about_belt')
    list_display_links = ()
    search_fields = ('kyu', 'color')

class nf(admin.ModelAdmin):

    list_display = ('id', 'kata','hits','blocks',)
    list_display_links = ('id', 'kata')
    search_fields = ('id', 'info_id', 'kata')


admin.site.register(Dictionary, di)
admin.site.register(Belt, blt)
admin.site.register(Info, nf)

