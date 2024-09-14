from django.http import HttpResponse
import datetime
from django.template import Template, Context


def saludo(request):

    nombres="Carlos"

    doc_externo=open("C:/Users/CARLO/Desktop/proyectosDjango/Proyecto1/index.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre_persona": nombres})

    document = plt.render(ctx)

    return HttpResponse(document)

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