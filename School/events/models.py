from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='company_posts/', blank=True, null=True)
    location = models.CharField(max_length=255)
    event_date = models.DateField()
    registration_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('title', 'description')  # Prevent same title+description

    def __str__(self):
        return self.title

