from django.contrib import admin
from django.urls import path

from landingpage import views as landing
from accounts import views as accounts
from tastings import views as tastings

urlpatterns = [
    # Landing page
    path('', landing.landing, name='landing'),
    # Wines
    path('wines/', tastings.WineList.as_view(), name='wines'),
    # Events
    path('events/', tastings.EventList.as_view(), name='events'),
    # TastingNotes
    path('tastingnotes/', tastings.tasting_notes, name='notes'),
    # Account management/logins
    path('accounts/login/', accounts.Login.as_view(), name='login'),
    path('accounts/logout/', accounts.Logout.as_view(), name='logout'),
    path('accounts/signup/', accounts.Signup.as_view(), name='signup'),
    path('accounts/profile/', accounts.Profile.as_view(), name='profile'),
    # Admin page
    path('admin/', admin.site.urls, name='admin'),
]
