import json
import requests

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from book.serializers import BookSerializer
from book.models import Book


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CURD operations regarding local data base
    """
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country', 'publisher', 'released']

    def get_queryset(self):
        return Book.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Overriding method to customize response
        """
        response_instance = super(BookViewSet, self).list(request)
        return Response({"status": status.HTTP_200_OK, "message": "success", "data": response_instance.data})

    def retrieve(self, request, *args, **kwargs):
        """
        Overriding method to customize response
        """
        response_instance = super(BookViewSet, self).retrieve(request)
        return Response({"status": status.HTTP_200_OK, "message": "success", "data": response_instance.data})

    def create(self, request, *args, **kwargs):
        """
        Overriding method to customize response
        """
        sec = request.data
        request.data['numberOfPages'] = sec['number_of_pages']
        request.data['released'] = sec['release_date']
        response_instance = super(BookViewSet, self).create(request)
        return Response({"status": status.HTTP_201_CREATED, "message": "success", "data": response_instance.data})

    def partial_update(self, request, *args, **kwargs):
        """
        Overriding method to customize response
        """
        response_instance = super(BookViewSet, self).partial_update(request)
        return Response({"status": status.HTTP_200_OK,
                         "message": f"The book {response_instance.data['name']} was updated successfully",
                         "data": response_instance.data})

    def destroy(self, request, *args, **kwargs):
        """
        Overriding method to customize response
        """
        instance = self.get_object()
        instance.delete()
        return Response({"status": status.HTTP_200_OK,
                         "message": f"The book {instance.name} was deleted successfully",
                         "data": []})


class BookDeleteViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling delete operation for book.
    """
    serializer_class = BookSerializer

    def delete_book(self, request, *args, **kwargs):
        book_id = kwargs.get('id', None)
        status_code = status.HTTP_200_OK
        try:
            data_ins = Book.objects.get(id=book_id)
            message = f"The book {data_ins.name} was deleted successfully"
            data_ins.delete()
        except ObjectDoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            message = "Requested entity does not exist"
        return Response(
            {"status": status_code, "message": message, "data": []})


class IceAndFireAppViewSet(viewsets.GenericViewSet):
    """
    Ice and Fire api ViewSet. This is used to get data from ice and fire api
    """
    serializer_class = BookSerializer
    ICE_AND_FIRE_URL = 'https://www.anapioficeandfire.com/api/books'

    def get_book_from_ice_and_fire(self, request):
        try:
            name_of_book = request.GET.get('name')
            url = f"{self.ICE_AND_FIRE_URL}/?name={name_of_book}"
            server_response = requests.get(url, headers={'content-type': 'application/json'})
            data_ins = json.loads(server_response.content)
            serialize_ins = BookSerializer(data=data_ins, many=True)
            serialize_ins.is_valid(raise_exception=True)
            return Response(
                {"status": server_response.status_code, "message": "success", "data": serialize_ins.data})
        except Exception:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
