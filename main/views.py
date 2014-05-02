from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import UPC, LookupSites, CustomerReviews

def list_upc(request):
    upc_codes = UPC.objects.all()
    return render_to_response('list_upc.html',{'upc_codes':upc_codes},context_instance=RequestContext(request))

def list_sites(request):
    lookup_sites = LookupSites.objects.all()
    return render_to_response('list_sites.html',{'lookup_sites':lookup_sites},context_instance=RequestContext(request))

def upc_reviews(request,code):
    upc_details = UPC.objects.get(pk=code)
    reviews = CustomerReviews.objects.filter(upc_id=upc_details.id)
    lookup_sites = LookupSites.objects.all()
    return render_to_response('upc_reviews.html',{'reviews':reviews,
                                                  'product':upc_details,
                                                  'lookupsites':lookup_sites,
                                                   'code':code
                                                  },
                              context_instance=RequestContext(request))