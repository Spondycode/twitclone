from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Meep

# Unregister Groups
admin.site.unregister(Group)

# mix profile info with the user info
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]

# Unregister initial user
admin.site.unregister(User)

# admin.site.register(Profile)
admin.site.register(User, UserAdmin)


admin.site.register(Meep)
