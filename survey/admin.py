from django.contrib import admin

from .models import InitialSurveyResponse

class InitialSurveyAdmin(admin.ModelAdmin):
    fields = ['name',
              'email',
              'favoritewine']

admin.site.register(InitialSurveyResponse, InitialSurveyAdmin)
