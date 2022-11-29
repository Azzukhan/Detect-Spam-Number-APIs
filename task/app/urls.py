from rest_framework import routers
from app.views import TestUser, SpamViewSet, UserViewSet, SearchNameViewSet, SearchNumberViewSet

urlpatterns = []
router = routers.SimpleRouter()
router.register("search",SearchNameViewSet,basename="SearchNameViewSet")
router.register("search",SearchNumberViewSet,basename="SearchNumberViewSet")
router.register("user",UserViewSet,basename="UserViewSet")
router.register("spam",SpamViewSet,basename="SpamViewSet")
router.register("test",TestUser,basename="TestUserViewSet")
urlpatterns+=router.urls
