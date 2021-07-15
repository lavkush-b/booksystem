from collections import OrderedDict
from datetime import datetime
from rest_framework import serializers
from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    """
    Book Serializer is using for serializing or deserializing book data
    """
    number_of_pages = serializers.SerializerMethodField()
    release_date = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "name", "isbn", "authors", "country", "number_of_pages", "publisher", "release_date"]

    def get_number_of_pages(self, obj):
        """
        Getting number of pages from instance
        :param obj: data instance
        """
        try:
            if isinstance(obj, OrderedDict):
                obj = dict(obj)
                return obj['numberOfPages']
            return obj.numberOfPages
        except KeyError:
            return 0

    def get_release_date(self, obj):
        """
        Getting number of pages from instance
        :param obj: data instance
        """
        try:
            if isinstance(obj, OrderedDict):
                obj = dict(obj)
                return obj['released']
            return obj.released
        except KeyError:
            return datetime.now()
