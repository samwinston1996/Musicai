from django.db import models


class AI_Model(models.Model):
    display_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "AI Models"
        verbose_name_plural = "AI Models"

    def __str__(self):
        return self.display_name