from django.contrib import admin

from profiles_api import models
# for regiter to admin ui site 
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)

# Register your models here.
