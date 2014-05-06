from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from main.models import UPC, LookupSites, CustomerReviews
from forms import CustomerReviewForm
from django.http import HttpResponseRedirect

def list_upc(request):
    upc_codes = UPC.objects.all()
    return render_to_response('list_upc.html',{'upc_codes':upc_codes},context_instance=RequestContext(request))

def list_sites(request):
    lookup_sites = LookupSites.objects.all()
    return render_to_response('list_sites.html',{'lookup_sites':lookup_sites},context_instance=RequestContext(request))


def upc_reviews(request,code):
    upc_details = UPC.objects.get(pk=code)

    currentsiteid='All'

    if ('lookupsiteid' in request.GET) and (request.GET['lookupsiteid'] !='All'):
        reviews = CustomerReviews.objects.filter(upc_id=upc_details.id).filter(lookupsite_id=request.GET['lookupsiteid'])
        currentsiteid = request.GET['lookupsiteid']
    else:
        reviews = CustomerReviews.objects.filter(upc_id=upc_details.id)

    new_review = CustomerReviewForm()

    lookup_sites = LookupSites.objects.all()

    return render_to_response('upc_reviews.html',{'reviews':reviews,
                                                  'product':upc_details,
                                                  'lookupsites':lookup_sites,
                                                   'code':code,
                                                   'currentsiteid':currentsiteid,
                                                   'new_review': new_review
                                                  },
                              context_instance=RequestContext(request))

def add_review(request):
    if request.method == 'POST':
        form = CustomerReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            code = request.POST['code']
            new_review.upc= UPC.objects.get(pk=code)
            new_review.lookupsite = LookupSites.objects.get(pk=4)
            new_review.save()
    else:
        form=CustomerReviewForm()

    redirect_url = "/upc_reviews/" + request.POST['code']

    return HttpResponseRedirect(redirect_url)