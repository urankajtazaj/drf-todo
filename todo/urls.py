from django.urls import include, path
from todo import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
