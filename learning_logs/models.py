from django.db import models


class Topic(models.Model):
    """Topic being learnt by the user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return representation of the model as a string"""
        return self.text


class Entry(models.Model):
    """Specific information about progress in learning"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return representation of the model as a string"""
        if len(self.text) < 50:
            return self.text
        else:
            return f"{self.text[:50]}..."
