from django.shortcuts import render,redirect
import PyPDF2
from django.http import HttpResponse
from .models import Pdf
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from .serializers import PdfSerializer#, StandardsSerializer, CountriesSerializer, TagSerializer

from .models import Pdf#, Standards, Countries, Tag

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status





class PdfList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        currencies = Pdf.objects.all()
        serializer = PdfSerializer(currencies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PdfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PdfDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Pdf.objects.get(pk=pk)
        except Pdf.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        currencies = self.get_object(pk)
        serializer = PdfSerializer(currencies)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        currencies = self.get_object(pk)
        serializer = PdfSerializer(currencies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    documents = Pdf.objects.all()
    #rank = Document.objects.latest('id')
    #print(rank)
    for obj in documents:
        rank = obj.link
        num  =  obj.data 
        document = obj.description
    print(num)
    filename =  './media/'+str(num)
    pdf = PyPDF2.PdfReader((filename))
    page = pdf.pages[0].mediabox
# print(page.width)
# print(page.height)
# value = 'Landscape'
    #value = 'Landscape'
    value = document
    if 'Portrait' == value:
        print('Portrait')
        new_filename = pdf360(filename)
    else:
        print('Landscape')
        new_filename = pdf180(filename)
    return HttpResponse("Hello, world!")


def pdf180(filename):
    with open(filename, 'rb') as file:
        # Create PDF reader object
        #pdf = PyPDF2.PdfFileReader(file)
        pdf = PyPDF2.PdfReader(file)
        # Get the number of pages in the PDF file
        pages = len(pdf.pages)
        # Create PDF writer object
        mirror = PyPDF2.PdfWriter()
        # Mirror each page horizontally and add it to the mirrored object
        for i in range(pages):
            page = pdf.pages[i]
            page.rotate(180)
            page.scale(-1, 1)
            mirror.add_page(page)
        # Create a new file name and write the converted PDF to the new file
        new_filename = filename[:-4] + '_horizontal_mirror.pdf'
        with open(new_filename, 'wb') as output:
            mirror.write(output)
        # Return the new file name
        return new_filename

def pdf360(filename):
    with open(filename, 'rb') as file:
        # Create PDF reader object
        #pdf = PyPDF2.PdfFileReader(file)
        pdf = PyPDF2.PdfReader(file)
        # Get the number of pages in the PDF file
        pages = len(pdf.pages)
        # Create PDF writer object
        mirror = PyPDF2.PdfWriter()
        # Mirror each page horizontally and add it to the mirrored object
        for i in range(pages):
            page = pdf.pages[i]
            page.rotate(360)
            page.scale(-1, 1)
            mirror.add_page(page)
        # Create a new file name and write the converted PDF to the new file
        new_filename = filename[:-4] + '_horizontal_mirror.pdf'
        with open(new_filename, 'wb') as output:
            mirror.write(output)
        # Return the new file name
        return new_filename






