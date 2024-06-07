from django.db import models

class Modality(models.Model):
    modality_specialization = models.ForeignKey(
        'users.Specialization', on_delete=models.CASCADE,
        )
    modality = models.CharField(max_length=255)

    def __str__(self):
        return self.modality    

class MedicalExamination(models.Model):
    examination_modality = models.ForeignKey(Modality, on_delete=models.CASCADE)
    examination_type = models.CharField(max_length=100, blank=True, null=True)
    conventional_units = models.DecimalField(
        max_digits=3, decimal_places=1, default=1
        )
    def __str__(self):
        return f'{self.examination_modality}: {self.examination_type}'