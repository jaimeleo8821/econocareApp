from django.contrib import admin
from .models import Type, Category, Pay_Method, Movement

class MovementAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()

# Register your models here.
admin.site.register(Movement, MovementAdmin)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Pay_Method)
