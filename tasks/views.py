from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Task,Note
from .serializers import TaskSerializer,NoteSerializer
# Create your views here.


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user.id)

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}

class NoteViewSet(ModelViewSet):
    serializer_class=NoteSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user_id=self.request.user.id)

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}
