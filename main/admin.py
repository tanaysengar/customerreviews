from django.contrib import admin
from main.models import UPC, LookupSites, CustomerReviews

class UPCAdmin(admin.ModelAdmin):
    class Meta:
        model= UPC

class LookupSitesAdmin(admin.ModelAdmin):
    class Meta:
        model= LookupSites

class CustomerReviewsAdmin(admin.ModelAdmin):
    list_display = ('review','upc','lookupsite')
    class Meta:
        model= CustomerReviews

admin.site.register(UPC,UPCAdmin)
admin.site.register(CustomerReviews,CustomerReviewsAdmin)
admin.site.register(LookupSites,LookupSitesAdmin)