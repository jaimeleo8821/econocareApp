from django.contrib import admin
from .models import Type, Category, Pay_Method, Movement, Origin

class MovementAdmin(admin.ModelAdmin):
    readonly_fields = ('idUser',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()

# Register your models here.
admin.site.register(Movement, MovementAdmin)
admin.site.register(Origin)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Pay_Method)

# CONFIGURACIÓN DEL PANEL
title = "EconoCare"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
