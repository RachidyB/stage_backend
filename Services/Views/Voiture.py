from rest_framework.decorators import api_view
from Services.serializers import *
from Services.models import *
from rest_framework.response import Response



#Voiture Api


@api_view(['GET'])
def ShowAll(request):
    Voitures = Voiture.objects.all()
    serializer = VoitureSerializer(Voitures, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewVoitureBymatricule(request, pk):
    Voitures= Voiture.objects.get(Matricule=pk)
    serializer = VoitureSerializer(Voitures, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def ViewVoitureByMarque(request, marque):
    Voitures= Voiture.objects.get(Marque=marque)
    serializer = VoitureSerializer(Voitures, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateVoiture(request):
    serializer = VoitureSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def updateVoiture(request, pk):
    Voitures = Voiture.objects.get(matricule=pk)
    serializer = VoitureSerializer(instance=Voitures, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteVoiture(request, pk):
    Voitures = Voiture.objects.get(Matricule=pk)
    Voitures.delete()

    return Response('Items delete successfully!')