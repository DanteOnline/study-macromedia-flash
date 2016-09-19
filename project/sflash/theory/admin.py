from django.contrib import admin
from theory.models import Theory

# Register your models here.
class TheoryAdmin(admin.ModelAdmin):
    list_display = ['parent','name']
admin.site.register(Theory, TheoryAdmin)
