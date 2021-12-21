from django.db import models


class Classes(models.Model):

    class Meta:
        verbose_name_plural = 'Classes'

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price_per_block = models.DecimalField(
        max_digits=6, decimal_places=2)
    price_per_class = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class PersonalTrainers(models.Model):

    class Meta:
        verbose_name_plural = 'Personal Trainers'

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    qualifications = models.TextField(
        max_length=254, null=True, blank=True)
    price_per_session = models.DecimalField(max_digits=6, decimal_places=2)
    price_per_block_4 = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    price_per_block_8 = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    price_per_block_12 = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    email_address = models.EmailField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
