from django.contrib import admin

from .models import BowdoinWineUser

class BowdoinWineUserAdmin(admin.ModelAdmin):
    fields = ['first_name',
              'last_name',
              'private_name',
              'username',
              'email',]

admin.site.register(BowdoinWineUser, BowdoinWineUserAdmin)
