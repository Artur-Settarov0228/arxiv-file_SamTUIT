from django.db import models

class Talabalar(models.Model):
    CHOISE_FACULTY = (
        ('Kompyuter injiniring', 'kompyuter injiniring'),
        ('Axborot texnologiyalar', 'axborot texnologiyalar')
    )
    CHOISE_STATUS = (
        ('O‘qimoqda', 'o‘qimoqda'),
        ('Bitirgan', 'bitirgan'),
        ('To‘xtatgan', 'to‘xtatgan')
    )

    full_name = models.CharField(max_length=300)
    pasport = models.CharField(max_length=9)
    qabul_yili = models.IntegerField(max_length=4)
    faculty = models.CharField(choices=CHOISE_FACULTY)
    group = models.CharField(max_length=128)
    status = models.CharField(choices=CHOISE_STATUS)


    def __str__(self):
        return f"{self.id}.{self.full_name}"
