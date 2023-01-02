from django.db import models
from django.contrib.auth.models import AbstractUser

class BowdoinWineUser(AbstractUser):
    private_name = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" if not self.private_name else "Anonymous"
