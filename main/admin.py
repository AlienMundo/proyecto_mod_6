from django.contrib import admin
from main.models import Cliente, Flan


# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
  pass

admin.site.register(Cliente, ClienteAdmin)

class FlanAdmin(admin.ModelAdmin):
  pass


admin.site.register(Flan, FlanAdmin)