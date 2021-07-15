from django.conf.urls import url, include

from book.views import BookViewSet, BookDeleteViewSet, IceAndFireAppViewSet
from rest_framework.routers import DefaultRouter

book_router = DefaultRouter()
book_router.register(r'', BookViewSet, basename='books')
delete_book = BookDeleteViewSet.as_view({
    'post': 'delete_book'
})
get_book_from_ice_and_fire = IceAndFireAppViewSet.as_view({
    "get": "get_book_from_ice_and_fire"
})
urlpatterns = [
    url(r'^api/v1/books/', include(book_router.urls)),
    url(r'^api/v1/books/(?P<id>\d+)/delete/$', delete_book, name='delete_book'),
    url(r'^api/external-books/$', get_book_from_ice_and_fire, name='ice_and_fire')
]
