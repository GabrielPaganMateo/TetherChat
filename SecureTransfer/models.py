from django.db import models

# Create your models here.
class message:
    # Sender ID
    sender = None
    # Receiver ID
    receiver = None
    # Message str
    text = None
    # Status (read/unread) bool
    unread = None