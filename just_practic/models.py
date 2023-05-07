from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Car(models.Model):
    brend = models.CharField(verbose_name='brand', max_length=100)
    color = models.CharField(verbose_name='color', max_length=100)
    velume = models.CharField(verbose_name='Обьем',db_index=True, unique=True, max_length=100)
    image = models.ImageField(verbose_name='image', upload_to='images/car')
    TYPE_CAR = (
        (1, 'Седан'),
        (2, 'Хечбек'),
        (3, 'Универсал'),
        (4, 'Купе')
    )
    car_type = models.IntegerField(verbose_name='Пользователь', choices=TYPE_CAR)
    user = models.ForeignKey(User, on_delete=models.CASCADE)