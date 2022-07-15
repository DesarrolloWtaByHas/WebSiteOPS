from pydoc import plain
from django.shortcuts import render
from isla_N.models import PlanesServiciosEspeciales, PlanesKonecta,PlanesWTA,PlanesMorarbe, NumerosAxxaAssistance

# Create your views here.

def base(request):
    return render(request, 'base.html')

def islaN(request):
    return render(request, 'isla_N/tpaN.html')

def islaNRiesgo(request):
    return render(request, 'isla_N/riesgoN.html')
    
def islaU(request):
    return render(request, 'isla_U/riesgoU.html')

def islaE(request):
    return render(request, 'isla_E/riesgoE.html')

def islaEtpa(request):
    return render(request, 'isla_E/tpaE.html')

def islaUtpa(request):
    return render(request, 'isla_U/tpaU.html')

def serviciosEspeciales(request):
    especiales = PlanesServiciosEspeciales.objects.all()
    konectas = PlanesKonecta.objects.all()
    wtas = PlanesWTA.objects.all()
    morarbes = PlanesMorarbe.objects.all()
    numerosAxxa = NumerosAxxaAssistance.objects.all()
    context = {
        'especiales': especiales,
        'konectas': konectas,
        'wtas': wtas,
        'morarbes': morarbes,
        'numerosAxxa': numerosAxxa,
    }
    return render(request, 'serviciosEspeciales/riesgosEspeciales.html', context)

def prueba(request):
    return render(request, 'prueba.html')