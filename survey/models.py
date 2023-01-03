from django.db import models

class InitialSurveyResponse(models.Model):
    name = models.CharField(max_length=200, 
                            verbose_name="What is your name?")
    email = models.EmailField(unique=True, 
                              primary_key=True,
                              verbose_name="What is your Bowdoin email address?")
    meeting_prefs_choices = (
        (0, "Weekly"),
        (1, "Biweekly"),
        (2, "Monthly"),
    )
    meeting_preference = models.IntegerField(choices=meeting_prefs_choices, verbose_name="How often would you like to meet?")
    oneglassorseveral_choices = (
        (0, "One glass of one wine"),
        (1, "One glass of a selection of wines"),
        (2, "Several small pours"),
    )
    oneglassorseveral = models.IntegerField(choices=oneglassorseveral_choices, verbose_name="Would you prefer to drink one glass of a selected wine, one glass of your choice of a selection of wines, or several smaller pours of multiple wines?")
    pay_choices = (
        (0, "$0"),
        (1, "$1-$5"),
        (2, "$6-$10"),
    )
    pay = models.IntegerField(choices=pay_choices, verbose_name="How much would you be willing to pay to attend? (We don't have funding due to the illegal nature of the club, but the price will likely be very low! $1-5 range)")
