from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import UPC

def list_upc(request):
    upc_codes = UPC.objects.all()
    return render_to_response('list_upc.html',{'upc_codes':upc_codes},context_instance=RequestContext(request))

def fluid(request):
    return render_to_response('fluid.html',{'upc_codes':12},context_instance=RequestContext(request))

