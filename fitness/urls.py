from django.urls import path
from .views import UserListCreateView, WorkoutListCreateView, WorkoutDetailView, UserProfileView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('workouts/', WorkoutListCreateView.as_view(), name='workout-list-create'),
    path('workouts/<int:pk>/', WorkoutDetailView.as_view(), name='workout-detail'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),  
]
