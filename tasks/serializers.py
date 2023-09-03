from rest_framework import serializers
from .models import Task,Note


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']

    def create(self, validated_data):
        
        return Task.objects.create(user_id=self.context['user_id'],
                                    **self.validated_data)

class NoteSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model=Note
        fields = ['id', 'title', 'note', 'image', 'created_at']


    def create(self, validated_data): 
        return Note.objects.create(user_id=self.context['user_id'], 
                                   **self.validated_data)

