from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class TestModel(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'\+998\s\d{2}\s\d{3}\s\d{2}\s\d{2}',
                                 message='Phone number must be entered in the format: "+998 99 999 99 99".'
                                         'Up to the 12 digits allowed.')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    is_alive = models.BooleanField()
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    extra_name = models.CharField(max_length=255, editable=False, default='null')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = 'Test Model'

    def save(self, *args, **kwargs):
        self.extra_name = f'{self.name} | {self.is_alive}'
        super().save(*args, **kwargs)


class ModelX(models.Model):

    test_content = models.ForeignKey(TestModel, on_delete=models.CASCADE, related_name='test_content_x')
    mileage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.test_content.name} | {self.mileage}'

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = 'Model X'


class ModelY(models.Model):

    test_content = models.OneToOneField(TestModel, on_delete=models.CASCADE, related_name='test_content_y')
    mileage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.test_content.name} | {self.mileage}'

    class Meta:
        ordering = ('created_at',)
        verbose_name_plural = 'Model Y'
