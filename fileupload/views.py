from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from fileupload.models import Document
from fileupload.forms import DocumentForm

import csv
import os
from django.conf import settings

from main.models import UPC

def list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            print(newdoc.docfile)
            handle_file(newdoc.docfile)
            return HttpResponseRedirect('/list_upc')
    else:
        form = DocumentForm()
        documents = Document.objects.all()

        return render_to_response('list.html',
            {'documents':documents,
             'form': form
            },
            context_instance=RequestContext(request)
        )


def handle_file(dataFile):
    #reader = csv.DictReader(open(os.path.join(SITE_ROOT,dataFile))

    #dataReader = csv.reader(open('/Users/tanaysengar/Programming/PythonProjects/customerreview/media/document/2014/04/18/Workbook3_3.csv'),
    #                        delimiter=',',
    #                       quotechar='"')

    filepath = dataFile.path

    print filepath

    dataReader = csv.reader(open(filepath,"rU"),delimiter=',',quotechar='"')

    for row in dataReader:
        if row[0] != 'UPC':
            upccode = UPC()
            upccode.code = row[0]
            upccode.save()
