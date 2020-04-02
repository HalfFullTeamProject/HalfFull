from django.contrib import admin

# Register your models here.
from HalfFull.models import UserProfile, Pub, Crawl

admin.site.register(Pub)
admin.site.register(UserProfile)
admin.site.register(Crawl)
