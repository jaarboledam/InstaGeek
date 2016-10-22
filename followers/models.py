from django.contrib.auth.models import User
from django.db import models


class Relationship(models.Model):

    origin = models.ForeignKey(User, related_name='relationship_origin')  # usuario que sigue
    target = models.ForeignKey(User, related_name='relationship_target')  # usuario al que sigue
    created_at = models.DateTimeField(auto_now_add=True)
