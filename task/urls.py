from django.urls import path
from task import views


urlpatterns = [
    path('profile/', views.ProfileListView.as_view()),
    path('profile/<int:pk>', views.ProfileDetailUpdateDeleteView.as_view()),
    path('task/', views.TaskListCreateView.as_view()),
    path('task/<int:pk>', views.TaskDetailUpdateDeleteView.as_view()),
]
