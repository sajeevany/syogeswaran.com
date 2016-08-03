from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def home(request):
    return render_to_response('syogesweb/home.html', context_instance=RequestContext(request));


def apps(request):
    return render_to_response('syogesweb/appsMenu.html', context_instance=RequestContext(request));


def contact(request):
    return render_to_response('syogesweb/contact.html', context_instance=RequestContext(request));


def about(request):
    return render_to_response('syogesweb/about.html', context_instance=RequestContext(request));
