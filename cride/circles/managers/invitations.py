""" Circle Invitations """

# Django
from django.db import models

# Utilities
import random
from string import ascii_uppercase, digits


class InvitationManager(models.Manager):
    """ 
        Invitation Manager 
        Used to handle Code Creation
    """

    CODE_LENGHT = 10

    def create(self, **kwargs):
        """ Handle Code Cretion """
        pool = ascii_uppercase + digits + '.-'
        code = kwargs.get('code', ''.join(random.choices(pool, k=self.CODE_LENGHT)))
        while self.filter(code=code).exists():
            code = kwargs.get('code', ''.join(random.choices(pool, k=self.CODE_LENGHT)))
        kwargs['code'] = code
        return super(InvitationManager, self).create(**kwargs)
