from django.urls import path ,include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('books/', include(router.urls) )
]