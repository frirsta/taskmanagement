from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from api.permissions import IsOwner, IsAdmin
from .models import Task, Profile
from .serializers import TaskSerializer, ProfileSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = [
        'status',
        'priority',
        'created_date',
        'due_date',
    ]
    filterset_fields = [
        'owner__profile',
        'status',
        'priority',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwner]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = [
        'owner__profile',
        'due_date',
        'priority',
        'status',
    ]
    search_fields = [
        'owner__username',
        'title',
        'assigned_to',
    ]


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdmin]


class ProfileDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]
