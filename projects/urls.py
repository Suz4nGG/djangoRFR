from rest_framework import routers
from projects.api import ProjectViewSet

router = routers.DefaultRouter()

# ? Registramos las rutas
router.register("api/projects", ProjectViewSet, "projects")

# * De igual forma agregamos el urlpatterns y rest se encarga de crearlas
urlpatterns = router.urls
