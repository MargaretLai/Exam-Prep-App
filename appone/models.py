from django.db import models

# Create your models here.
class Review(models.Model):
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject
    
    
class Prep(models.Model):
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject
    
class EmailSubscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email