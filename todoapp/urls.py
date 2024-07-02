from django.urls import include, path
from todo import urls


urlpatterns = [
    path('', include(urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
