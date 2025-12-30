from django.db import models

class VQaror(models.Model):
    qaror_num = models.CharField(unique=True, null=False)
    title = models.CharField()
    created_at = models.DateTimeField()
    description = models.CharField()
    file = models.FileField(upload_to="VQarorlar/")

    class Meta:
        verbose_name = "Vazirlik Qarorlari"

    
    def __str__(self):
        return f"{self.id}. {self.qaror_num} ------ {self.title}"
