from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
import os
import json

from .models import GeoArea

# Create your views here.


def index(request):
    return HttpResponse("nothing is finished")


def demo(request):
    return render(request, 'maps/demo.html')


def area(request, c):
    try:
        area = GeoArea.objects.get(code=c)
        filename = _geojson_filename(area.level, c)
        obj = _load_jsonfile(filename)
    except GeoArea.DoesNotExist:
        raise Http404("Area with code %s cannot be found." % c)
    except:
        raise Http404("Area with code %s JSON file cannot be found" % c)

    return _return_jsonp_response(obj)


def areas(request, c1, c2):
    try:
        area1 = GeoArea.objects.get(code=c1)
        area2 = GeoArea.objects.get(code=c2)
        filename1 = _geojson_filename(area1.level, c1)
        filename2 = _geojson_filename(area2.level, c2)

        obj1 = _load_jsonfile(filename1)
        obj2 = _load_jsonfile(filename2)
        obj1['features'] = obj1['features'] + obj2['features']
    except GeoArea.DoesNotExist:
        raise Http404("Area with code %s cannot be found." % c)
    except:
        raise Http404("Area with code %s JSON file cannot be found" % c)

    return _return_jsonp_response(obj1)


def _geojson_filename(level, code):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if level == 1:
        filename = base_dir + "/china-cities/datas/%d.json" % code
    elif level == 2:
        p = (code // 10000) * 10000
        filename = base_dir + "/china-cities/datas/%d/%d.json" % (p, code)
    else:
        filename = ""

    return filename


def _load_jsonfile(filename):
    f = open(filename)
    jsonstr = f.read()
    jsonstr = jsonstr.replace("\ufeff", "")
    f.close()
    return json.loads(jsonstr)


def _return_jsonp_response(obj):
    resp = JsonResponse(obj)
    resp['Access-Control-Allow-Origin'] = '*'
    return resp


