from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,NoteViewSet
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')
router.register('notes',NoteViewSet,basename='note')
urlpatterns = router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)