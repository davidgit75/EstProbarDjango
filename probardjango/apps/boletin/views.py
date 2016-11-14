from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.

def inicio(request):
    context = {}
    return render_to_response('inicio.html', context, context_instance=RequestContext(request))
