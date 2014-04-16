from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from fileupload.models import Document
from fileupload.forms import DocumentForm

def list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            return HttpResponseRedirect('list.html')
    else:
        form = DocumentForm()

        documents = Document.objects.all()

        return render_to_response('list.html',
            {'document':documents,
             'form': form
            },
            context_instance=RequestContext(request)

        )