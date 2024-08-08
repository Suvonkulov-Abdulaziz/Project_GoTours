from django.contrib import admin
from .models import Tickets, ContactView , CategoryFLightModel, FlightModel, TravelClassModel


# Register your models here.
@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ['id', 'hotel', 'location']
    list_display_links = ['id', 'hotel']
    search_fields = ['hotel']
    list_filter = ['hotel', 'location']
    readonly_fields = ['status']
    
@admin.register(ContactView)
class ContactViewAdmin(admin.ModelAdmin):
    pass


admin.site.register(CategoryFLightModel)
# @admin.site.register(FlightModel)
admin.site.register(TravelClassModel)


@admin.register(FlightModel)
class FlightModelAdmin(admin.ModelAdmin):
    list_display = ['flying_from', 'flying_to', 'departing']
    list_display_links = ['flying_from', 'flying_to']
    list_filter = ['travelClass', 'category']
