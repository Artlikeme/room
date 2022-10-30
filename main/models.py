from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField('namePerson',max_length=150)
    def __str__(self):
        return self.name

class Rooms(models.Model):
    name = models.CharField('name',max_length=150)
    price = models.IntegerField('price')
    active = models.BooleanField('active')

    def __str__(self):
        return f'{self.name}'

class Appointment(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    start = models.DateField(verbose_name=('Start date'))
    end = models.DateField(verbose_name=('End date'))

    def __str__(self):
        return f'{self.room.name} {self.person.name} c {self.start}\
                                                    до {self.end}'