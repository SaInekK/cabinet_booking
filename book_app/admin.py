from django.contrib import admin

from .models import Office, Cabinet, Workplace, Booking

# Register your models here.

admin.site.register(Office)
admin.site.register(Cabinet)
admin.site.register(Workplace)
admin.site.register(Booking)
