from rest_framework.decorators import api_view
from Services.serializers import *
from Services.models import *
from rest_framework.response import Response



#technician API

@api_view(['GET'])
def ShowAll(request):
    Technicians = Technician.objects.all()
    serializer = TechnicianSerializer(Technicians, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewTechnicianById(request, pk):
    Technicians= Technician.objects.get(id=pk)
    serializer = TechnicianSerializer(Technicians, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def ViewTechnicianByName(request, nom):
    Technicians= Technician.objects.get(Nom=nom)
    serializer = TechnicianSerializer(Technicians, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def ViewTechnicianByProfession(request, profession):
    Technicians= Technician.objects.get(Profession=profession)
    serializer = TechnicianSerializer(Technicians, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateTechnician(request):
    serializer = TechnicianSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def updateTechnician(request, pk):
    Technicians = Technician.objects.get(id=pk)
    serializer = TechnicianSerializer(instance=Technicians, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTechnician(request, pk):
    Technicians = Technician.objects.get(id=pk)
    Technicians.delete()

    return Response('Items delete successfully!')