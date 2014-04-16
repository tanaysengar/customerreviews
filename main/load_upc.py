import sys, os

sys.path.append('/Users/tanaysengar/Programming/PythonProjects/customerreview/customerreview')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from main.models import UPC

import csv


dataReader = csv.reader(open(path), delimiter=',', quotechat='"')

for row in dataReader:
    if row[0] != 'UPC':
        upccode = UPC()
        upccode.code = row[0]
        upccode.save()