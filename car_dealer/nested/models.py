from django.core.validators import MinValueValidator
from django.db import models


GEAR_SHIFT_BOX_CHOICES = (
    ('variator', 'Вариатор'),
    ('mechanical', 'МКПП'),
    ('auto', 'АКПП')
)


class AutoBrand(models.Model):
    """Модель марок автомобиля"""
    brand = models.CharField(
        max_length=150,
        blank=False,
        unique=True,
        verbose_name='Наименование марки автомобиля'
    )

    objects = models.Manager()

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'


class Auto(models.Model):
    """Модель автомобилей"""
    brand = models.ForeignKey(
        AutoBrand,
        on_delete=models.CASCADE,
        blank=False,
        default=1,
        verbose_name='Марка автомобиля'
    )
    model = models.CharField(
        max_length=150,
        blank=False,
        verbose_name='Модель автомобиля'
    )

    objects = models.Manager()

    def __str__(self):
        return f'{self.brand.brand} {self.model}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class AutoCharacters(models.Model):
    """Модель характеристик автомобиля"""
    auto = models.OneToOneField(
        Auto,
        on_delete=models.CASCADE,
        verbose_name='Автомобиль'
    )
    engine_capacity = models.FloatField(
        validators=[MinValueValidator(0.0), ],
        blank=False,
        verbose_name='Объем двигателя (в литрах)'
    )
    engine_power = models.PositiveIntegerField(
        blank=False,
        verbose_name='Мощность двигателя (лошадиных сил)'
    )
    gear_shift_box = models.CharField(
        choices=GEAR_SHIFT_BOX_CHOICES,
        max_length=150,
        blank=False,
        verbose_name='Тип коробки переключения передач'
    )
    release_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900), ],
        default='1990',
        blank=False,
        verbose_name='Год выпуска'
    )
    color = models.CharField(
        max_length=100,
        blank=False,
        verbose_name='Цвет'
    )

    objects = models.Manager()

    def __str__(self):
        return f'Характеристики автомобиля {self.auto}'

    class Meta:
        verbose_name = 'Характеристики автомобиля'
        verbose_name_plural = 'Характеристики автомобилей'
