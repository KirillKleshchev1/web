from django.db import models

# Create your models here.


class Reservation(models.Model):
    username = models.CharField('ФИО', max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=255)
    email = models.CharField('Почта', max_length=255)
    count = models.IntegerField('Количество столиков', default=1)
    date = models.DateField('Дата', max_length=255)
    time = models.IntegerField('Время начала брони')
    count_hour = models.IntegerField('На сколько часов', default=1)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'

