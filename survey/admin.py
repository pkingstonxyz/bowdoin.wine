from django.contrib import admin

from .models import InitialSurveyResponse

class InitialSurveyAdmin(admin.ModelAdmin):
    fields = ['name',
              'email',
              'meeting_preference',
              'oneglassorseveral',
              'pay']

admin.site.register(InitialSurveyResponse, InitialSurveyAdmin)
