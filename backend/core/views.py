from django.shortcuts import render
from rest_framework.response import Response
from .serializer import ProduitSerializer
from .models import Produit
from rest_framework import status, viewsets


# Create your views here.
class ProduitApi(viewsets.ViewSet):
    # GET qui renvoi une liste l'element 
    def list(self,request):
        stu=Produit.objects.all()
        serializer=ProduitSerializer(stu,many=True)
        return Response(serializer.data)
    # GET qui renvoi un seul element 
    def retreive(self, request, pk=None):
        id=pk
        if id is not None:
            stu=Produit.objects.get(id=id)
            serializer=ProduitSerializer(stu)
            return  Response(serializer.data)
    # POST  
    def create(self,request):
        serializer=ProduitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data  created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request,pk):
        id=pk
        stu=Produit.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})