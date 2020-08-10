from django.db import models


class Feedback(models.Model):
    theme = models.CharField(max_length=500)
    description = models.CharField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        """
             String for representing the MyModelName object (in Admin site etc.)
             """
        return self.theme
