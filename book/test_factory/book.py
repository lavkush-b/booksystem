import factory
from book.models import Book


class BookFactory(factory.django.DjangoModelFactory):
    """Factory class for Book model"""
    name = factory.Faker('name')

    class Meta:
        model = Book
