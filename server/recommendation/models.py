from django.db import models


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
