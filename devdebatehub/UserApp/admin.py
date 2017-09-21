from django.contrib import admin
from UserApp.models import *

admin.site.register(User)
admin.site.register(Person)
admin.site.register(Organisation)
admin.site.register(FollowingUser)
admin.site.register(UserActivity)
admin.site.register(Story)