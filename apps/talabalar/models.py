from django.db import models


class Talabalar(models.Model):

    CHOISE_FACULTY = (
        ('Kompyuter', 'Kompyuter injiniring'),
        ('Axborot', 'Axborot texnologiyalar'),
    )

    CHOISE_STATUS = (
        ('O‘qimoqda', 'O‘qimoqda'),
        ('Bitirgan', 'Bitirgan'),
        ('To‘xtatgan', 'To‘xtatgan'),
    )

    full_name = models.CharField(max_length=300)
    pasport = models.CharField(max_length=9)
    qabul_yili = models.IntegerField()

    faculty = models.CharField(
        max_length=50,
        choices=CHOISE_FACULTY
    )

    group = models.CharField(max_length=128)

    status = models.CharField(
        max_length=20,
        choices=CHOISE_STATUS
    )

    def __str__(self):
        return f"{self.id}. {self.full_name}"
