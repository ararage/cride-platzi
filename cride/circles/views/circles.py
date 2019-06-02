""" Circle Views """

# Django REST Framework
from rest_framework import viewsets

# Serializers
from cride.circles.serializers import CircleModelSerializer


# Models
from cride.circles.models import Circle


class CircleViewSet(viewsets.ModelViewSet):
    """ Circle View Set """
    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer
