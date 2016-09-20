from django.contrib import admin
from ttest.models import JuniorQuestion, JuniorAnswer, SeniorQuestion, SeniorAnswer, ProfiQuestion
# Register your models here.
class JQAdmin(admin.ModelAdmin):
    list_display = ['theme','text']
admin.site.register(JuniorQuestion, JQAdmin)

class JAAdmin(admin.ModelAdmin):
    list_display = ['question','text','is_true']
admin.site.register(JuniorAnswer,JAAdmin)

class SQAdmin(admin.ModelAdmin):
    list_display = ['theme','text']
admin.site.register(SeniorQuestion, SQAdmin)

class SAAdmin(admin.ModelAdmin):
    list_display = ['question','text','is_true']
admin.site.register(SeniorAnswer,SAAdmin)

class PQAdmin(admin.ModelAdmin):
    list_display = ['theme','text','answer']
admin.site.register(ProfiQuestion, PQAdmin)

