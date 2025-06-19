from django.db import models
from TrainingProgram.models import TrainingProgram

class programModules(models.Model):
    link = models.TextField()
    title = models.TextField()
    trainingProgram = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.link} {self.title} ({self.trainingProgram})"
