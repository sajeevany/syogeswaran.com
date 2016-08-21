from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse


# Create your views here.
def home(request):
    return render_to_response('syogesweb/home.html', context_instance=RequestContext(request));


def apps(request):
    tbeAppURL = reverse('TesseractBoxEditor:tbe',args=[], kwargs={})
    return render(request, 'syogesweb/appsMenu.html', {'tbeAppURL':tbeAppURL});


def contact(request):
    return render_to_response('syogesweb/contact.html', context_instance=RequestContext(request));


def about(request):
    return render_to_response('syogesweb/about.html', context_instance=RequestContext(request));
