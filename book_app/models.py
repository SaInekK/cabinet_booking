from django.contrib.auth.models import User

from django.db import models


class Office(models.Model):
    name = models.CharField(max_length=255, unique=True)  # , verbose_name='Office'

    def __str__(self):
        return f'Office {self.name}'


class Cabinet(models.Model):
    name = models.CharField(max_length=255,
                            unique=True)
    office = models.ForeignKey(Office,
                               on_delete=models.CASCADE)

    def __str__(self):
        return f'Cabinet {self.name}, Office {self.office.name}'


class Workplace(models.Model):
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)

    def __str__(self):
        return f'Cabinet {self.cabinet.name}, Workplace #{self.id}'


class Booking(models.Model):
    datetime_from = models.DateTimeField(verbose_name='Start of booking')
    datetime_to = models.DateTimeField(verbose_name='End of booking')
    booker = models.ForeignKey(User,
                               related_name='bookers',
                               on_delete=models.CASCADE)
    comment = models.CharField(verbose_name='Booker comment',
                               max_length=10000,
                               blank=True)
    workplace = models.ForeignKey(Workplace,
                                  verbose_name='Workplace',
                                  related_name='workplaces',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return f'Booking #{self.id}: Office {self.workplace.cabinet.office.name}, ' \
               f'Cabinet {self.workplace.cabinet.name}, Workplace #{self.workplace.id}, ' \
               f'{self.datetime_from} - {self.datetime_to}'
