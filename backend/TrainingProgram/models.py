from django.db import models

class TrainingProgram(models.Model):
    PROGRAM_TYPES = [
        ('learnership', 'Learnership'),
        ('internship', 'Internship'),
        ('skills_program', 'Skills Program'),
    ]

    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    program_name = models.CharField(max_length=200)
    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPES)
    duration = models.PositiveIntegerField(help_text="Duration in months")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not_started')

    def __str__(self):
        return f"{self.program_name} ({self.get_program_type_display()})"

class Certificate(models.Model):
    training_program = models.ForeignKey(TrainingProgram, on_delete=models.CASCADE, related_name="certificates")
    name = models.CharField(max_length=200)
    certificate_number = models.CharField(max_length=50, unique=True)
    offered_by = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} ({self.certificate_number})"