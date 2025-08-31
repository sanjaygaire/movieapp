from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("reviews", ReviewViewSet, basename="reviews")

urlpatterns = router.urls
