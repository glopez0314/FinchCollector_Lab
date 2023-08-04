from django.contrib import admin

# Register your models here.
from .models import Dog, Trick, Playdate

admin.site.register(Dog)
admin.site.register(Trick)
admin.site.register(Playdate)
