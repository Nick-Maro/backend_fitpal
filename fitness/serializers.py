from rest_framework import serializers
from .models import CustomUser, Workout

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'age', 'weight']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'user', 'workout_type', 'duration_minutes', 'date']