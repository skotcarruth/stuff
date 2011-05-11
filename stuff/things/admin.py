from things.models import Thing
from django.contrib import admin

class ThingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('The Item', {
            'fields': ('name', 'slug', 'description', 'condition', 'image',),
        }),
        ('The Story', {
            'fields': ('acquisition_date', 'disposition_date', 'story', 'retail_price', 'cost', 'current_value', 'price',),
        }),
        ('Metadata', {
            'fields': ('created_ts', 'updated_ts',),
        })
    )
    readonly_fields = ('created_ts', 'updated_ts',)
    list_display = ('name', 'acquisition_date', 'cost', 'price', 'created_ts',)
    date_hierarchy = 'acquisition_date'

admin.site.register(Thing, ThingAdmin)