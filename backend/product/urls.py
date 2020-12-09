from django.conf.urls import url, include
from django.urls import path
from .views import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'answares',ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('pendings/', ProductViewSet.as_view({'get': 'list'})),
    # path('processeds/', ProcessedsList.as_view()),
    # path('sugestoes/', Sugestoes.as_view({'post': 'post'}))
]