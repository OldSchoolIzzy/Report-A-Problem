from django.contrib.auth.models import User
from django.db import models


# Primary key is set by default if not explicitly set
class Ticket(models.Model):
    LOW = "L"
    MEDIUM = "M"
    HIGH = "H"

    PROBLEM_TYPES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High')
    ]

    SOLVED = 'S'
    UNSOLVED = 'U'
    PENDING = 'P'
    OPEN = 'O'

    STATUS_TYPES = [
        (SOLVED, 'Solved'),
        (UNSOLVED, 'Unsolved'),
        (PENDING, 'Pending'),
        (OPEN, 'Open')
    ]

    subject = models.TextField(max_length=255)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=15, default=LOW)
    buildingName = models.CharField(max_length=25)
    status = models.CharField(max_length=15, choices=STATUS_TYPES, default=UNSOLVED)
    description = models.TextField(max_length=255)
    problemType = models.CharField(max_length=15, choices=PROBLEM_TYPES)
    image = models.ImageField(upload_to='static/img', storage=None, max_length=100, blank=True)

    def __str__(self):
        return f'Ticket id: {self.id} Status: {self.status}'
