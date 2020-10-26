__all__ = ['ShortURL']

import hashlib
from datetime import datetime

from django.db import models


class ShortURL(models.Model):
    """Model for saving url and its sort code"""

    url = models.URLField()
    code = models.CharField(max_length=100, unique=True, blank=True)

    def generate_code(self):
        """Generating hash code from url"""

        # getting current date time to resolve conflict
        date_time = datetime.now()

        # ISO 8601 is an international standard to represent date time
        iso_8601_time = date_time.isoformat()
        patched_url = f'{self.url}:{iso_8601_time}'

        # hashing URL with SHA1 algorithm
        hashed_url = hashlib.sha1(patched_url.encode('UTF-8')).hexdigest()

        # trimming the HASH to make it sort
        self.code = hashed_url[:10]

    def save(self, *args, **kwargs):
        """Override save method for getting a default code"""

        # if not code generate
        if not self.code:
            self.generate_code()

        self.code = ''.join(char for char in self.code if char.isalnum())

        # call parent class method
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.url} [{self.code}]'
