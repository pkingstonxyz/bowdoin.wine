from django.db import models

class InitialSurveyResponse(models.Model):
    name = models.CharField(max_length=200, 
                            verbose_name="What is your name?")
    email = models.EmailField(unique=True, 
                              primary_key=True,
                              verbose_name="What is your Bowdoin email address?")
    favoritewine = models.CharField(max_length=200,
                                    blank=True,
                                   verbose_name="Favorite wine? (optional)")
