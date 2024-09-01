from django.urls import path ,include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('books/', include(router.urls) ),
    
    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]