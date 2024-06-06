from django.db import models
from django.contrib.auth import get_user_model


class Recommendation(models.Model):
    name = models.CharField('Название', max_length=128)
    text = models.TextField('текст')

    for_current_max_weight = models.IntegerField('Максимальный текущий вес', null=True, blank=True)
    for_current_min_weight = models.IntegerField('Минимальный текущий вес', null=True, blank=True)

    max_expected_weight = models.IntegerField('Максимальный желаемый вес', null=True, blank=True)
    min_expected_weight = models.IntegerField('Минимальный желаемый вес', null=True, blank=True)

    class Meta:
        db_table = 'Recommendation'
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекомендации'

    def __str__(self):
        return self.text[:20]


def loadMealsPhotoToUserFolder(instance, filename):
    return f'meals/{instance.user.email}/{filename}'


class Meal(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='meals', on_delete=models.CASCADE,
                             verbose_name='пользователь')
    name = models.CharField('название еды', max_length=128)

    calories = models.FloatField('количество каллорий')
    vitamins = models.FloatField('количесвто витаминов')
    minerals = models.FloatField('количество минералов')
    proteins = models.FloatField('количество белков')
    fats = models.FloatField('количесвто жиров')
    carbohydrates = models.FloatField('количесвто углеводов')

    photo = models.ImageField('фото', upload_to=loadMealsPhotoToUserFolder, null=True, blank=True, max_length=256)
    date = models.DateTimeField()

    class Meta:
        db_table = 'Meal'
        verbose_name = 'Прием пищи'
        verbose_name_plural = 'Приемы пищи'

    def __str__(self):
        return self.name
