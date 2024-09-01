from django.urls import path ,include
from .views import BookList

urlpatterns = [
    path('books/', include(BookList.as_view()), name='book_list' )
]