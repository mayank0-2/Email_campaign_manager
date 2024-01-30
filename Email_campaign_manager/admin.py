from django.contrib.auth.models import Group, User
from Email_campaign_manager.models import PlusUserDetail, PlusContent
from django.contrib import admin
from django.contrib.auth.models import Group, User

class contentAdmin(admin.ModelAdmin):       #declaring the view of the PlusContent in admin panel
    list_display = ('content_id', 'content')


class userAdmin(admin.ModelAdmin):          #declaring the view of the plusUserDetail in admin panel
    list_display = ('id', 'name', 'email', 'content_id')


admin.site.register(PlusUserDetail, userAdmin)
admin.site.register(PlusContent, contentAdmin)
admin.site.unregister(User)     #Removing default listing in admin panel
admin.site.unregister(Group)    #Removing default listing in admin panel
