from django.urls import include, path
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'cartorios', views.CartoriosViewSet)
router.register(r'adressess', views.AdressesViewSet)

# Wire up our API using automatic URL routing.

# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('cartorios1/', views.lista_cartorios),
    path('cartorios1/<str:text_uf>', views.lista_cartorios_uf),
    path('cartorios1/<str:text_uf>/<int:text_id>', views.lista_cartorios_id),
    path('cartorios1/<int:text_id>/', views.lista_cartorios_id1),
]