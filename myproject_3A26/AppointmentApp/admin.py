from django.contrib import admin
from .models import Appointment

# Register your models here.
#admin.site.register(Appointment) : enregistre mais ne te permet pas de personnaliser l'affichage dans l'interface d'administration
#@admin.register(Appointment) #enregistrement de la classe Appointment dans l'interface d'administration
#class AppointmentAdminPers(admin.ModelAdmin):
 #   list_display = ('reason', 'status', 'appointment_date', 'doctor', 'patient') #affiche les champs dans l'interface d'administration
  #  list_filter = ('status', 'appointment_date', 'doctor', 'patient') #filtre les champs dans l'interface d'administration
   # list_editable = ('status',) #permet de modifier le champ status dans l'interface d'administration
    #admin.site.register(Appointment, AppointmentAdminPers) #enregistrement de la classe AppointmentAdminPers dans l'interface d'administration
@admin.action(description='Confirm selected appointments') #permet de définir une action personnalisée pour confirmer les rendez-vous sélectionnés
def confirm_appointment(modeladmin, request, queryset):
    queryset.update(status='Confirmed') #met à jour le statut des rendez-vous sélectionnés en "Confirmed"


@admin.register(Appointment) #enregistrement de la classe Appointment dans l'interface d'administration
class AppointmentAdminPers(admin.ModelAdmin):
    actions = [confirm_appointment] #ajoute l'action confirm_appointment à la liste des actions disponibles dans l'interface d'administration
    list_display = ('reason', 'status', 'appointment_date', 'doctor', 'patient') #affiche les champs dans l'interface d'administration
    list_filter = ('status', 'appointment_date', 'doctor', 'patient') #filtre les champs dans l'interface d'administration
    list_editable = ('status',) #permet de modifier le champ status dans l'interface d'administration
    search_fields = ('reason', 'doctor__username', 'patient__username') #permet de rechercher dans les champs reason, doctor et patient
    ordering = ('-appointment_date',) #permet de trier les rendez-vous par date décroissante
    fieldsets = (
        ('Description', {
            'fields': ('reason', 'prescription', 'status')
        }),
        ('Date + Duration', {
            'fields': ('appointment_date', 'duration_minutes')
        }),
        ('Doctor / Patient', {
            'fields': ('doctor', 'patient')
        }),
        ("Planification", {
            'fields': ('created_at', 'updated_at'),
        })

    )
    readonly_fields = ('created_at', 'updated_at') #permet de rendre les champs created_at et updated_at en lecture seule
