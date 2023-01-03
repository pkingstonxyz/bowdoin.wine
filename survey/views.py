from django.views.generic import CreateView
from .models import InitialSurveyResponse

class Survey(CreateView):
    model = InitialSurveyResponse
    fields = [
        'name',
        'email',
        'meeting_preference',
        'oneglassorseveral',
        'pay',
    ]
    template_name = "survey/initial_survey.html"
    success_url = "/"
