from django.contrib import admin
from AppointmentApp.models import Appointment
from .models import Doctor, Patient, Speciality, User

#Register your models here.
admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Speciality)

class appointmentStacked(admin.StackedInline):
    model = Appointment
    extra = 1
class doctorPersoClass(admin.ModelAdmin):
    inlines = [appointmentStacked]
admin.site.register(Doctor, doctorPersoClass)
   

