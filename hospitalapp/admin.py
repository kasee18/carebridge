from django.contrib import admin

from hospitalapp.models import * #import all *

# Register your models here.
admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(ward)
admin.site.register(Appoint)
admin.site.register(contact)

