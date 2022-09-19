from rest_framework.decorators import api_view
from Services.serializers import *
from Services.models import *
from rest_framework.response import Response



#Service Api


@api_view(['GET'])
def ShowAll(request):
    Services = Service.objects.all()
    serializer = ServiceSerializer(Services, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewServiceById(request, pk):
    Services= Service.objects.get(id=pk)
    serializer = ServiceSerializer(Services, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def ViewServiceByTechnicianId(request, id):
    Services= Service.objects.get(Technician=id)
    serializer = ServiceSerializer(Services, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def ViewServiceByVoitureMatricule(request, matricule):
    Services= Service.objects.get(Voiture=matricule)
    serializer = ServiceSerializer(Services, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def ViewServiceByDateEntree(request, date):
    Services= Service.objects.get(Date_entrée=date)
    serializer = ServiceSerializer(Services, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def ViewServiceByDateSortie(request, date):
    Services= Service.objects.get(Date_sortie=date)
    serializer = ServiceSerializer(Services, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateService(request):
    serializer = ServiceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def updateService(request, pk):
    Services = Service.objects.get(id=pk)
    serializer = ServiceSerializer(instance=Services, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteService(request, pk):
    Services = Service.objects.get(id=pk)
    Services.delete()

    return Response('Items delete successfully!')