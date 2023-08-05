from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    bio = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.owner}'


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')

    def __str__(self):
        return self.file.name


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    )
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    owner = models.ForeignKey(
        User, related_name='tasks_created', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(
        max_length=20, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='not_started')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    completion_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='tasks', blank=True)
    notes = models.TextField(blank=True)
    attachments = models.ManyToManyField(
        'Attachment', related_name='tasks', blank=True)
    subtasks = models.ManyToManyField(
        'self', related_name='parent_task', symmetrical=False, blank=True)
    reminders = models.DateTimeField(null=True, blank=True)
    estimated_time = models.DurationField(null=True, blank=True)
    actual_time = models.DurationField(null=True, blank=True)
    recurring = models.BooleanField(default=False)
