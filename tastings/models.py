from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Wine(models.Model):
    brand = models.CharField(max_length=200, blank=True, null=True)
    producer = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    grape = models.CharField(max_length=50, blank=True, null=True)
    vintage = models.IntegerField(blank=True, null=True)

    fortified = models.BooleanField()
    sparkling = models.BooleanField()
    desert = models.BooleanField()
    color = models.CharField(max_length=5) #Red, White, or Rosé

    def __str__(self):
        vintage = self.vintage if self.vintage else "Unknown Vintage"
        return f"{self.brand} {self.name} - {vintage}"

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    wines = models.ManyToManyField(Wine)

    def __str__(self):
        return f"{self.title} - {self.date}"

class TastingNote(models.Model):
    RATINGS_CHOICES = [
        (1, "Horrible"),
        (2, "Not for me"),
        (3, "It was wine"),
        (4, "I liked it"),
        (5, "Loved it, new favorite"),
    ]
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    wine = models.ForeignKey(Wine, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(choices=RATINGS_CHOICES)
    thoughts = models.CharField(max_length=500, blank=True)
    def __str__(self):
        if self.author.first_name:
            return f"{self.author.first_name} | {self.wine} | {self.event}"
        else:
            return f"{self.author.username} | {self.wine} | {self.event}"
