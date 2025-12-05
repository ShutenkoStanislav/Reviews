from django.db import models

class Review(models.Model):
    username = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.username} - {self.date}"
    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
        ordering = "-date"

