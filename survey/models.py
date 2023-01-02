from django.db import models

class InitialSurveyResponse(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, primary_key=True)
    meeting_prefs_choices = (
        (0, "Weekly"),
        (1, "Biweekly"),
        (2, "Monthly"),
    )
    meeting_preference = models.IntegerField(choices=meeting_prefs_choices)
    oneglassorseveral_choices = (
        (0, "One glass"),
        (1, "Several"),
    )
    oneglassorseveral = models.IntegerField(choices=oneglassorseveral_choices)
    pay_choices = (
        (0, "$0"),
        (1, "$1-$5"),
        (2, "$6-$10"),
    )
    pay = models.IntegerField(choices=pay_choices)
