# fitness/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Workout(models.Model):
    WORKOUT_TYPES = [
        ('C', 'Cardio'),
        ('S', 'Strength'),
        ('F', 'Flexibility'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=1, choices=WORKOUT_TYPES)
    duration_minutes = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username}'s {self.get_workout_type_display()} workout"

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    # Aggiungi related_name per evitare conflitti
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # related_name univoco per evitare conflitti
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # related_name univoco per evitare conflitti
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username
