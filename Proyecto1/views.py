from django.http import HttpResponse
import datetime


def saludo(request):

    documento="""<html>
    <body>
    <h1>Hola, mundo</h1>
    </body>
    </html>"""

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego, mundo")


def dameFecha(request):
    
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h2>Fecha y hora actuales %s</h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, agno):
    edadActual=32
    periodo=agno-2024
    edadFutura=edadActual+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(agno, edadFutura)
    return HttpResponse(documento)