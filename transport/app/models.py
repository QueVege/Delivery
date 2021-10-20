from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'Company: {self.name}'

    class Meta:
        verbose_name_plural = 'Companies'


class Category(models.Model):

    CATEGORY_CHOICES = (
        ('a', 'A'), ('a1', 'A1'),
        ('b', 'B'), ('be', 'BE'),
        ('c1', 'C1'), ('c1e', 'C1E'),
        ('c', 'C'), ('ce', 'CE'),
        ('d1', 'D1'), ('d1e', 'D1E'),
        ('d', 'D'), ('de', 'DE'),
    )

    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='b', unique=True)

    def __str__(self):
        return f'Category: {self.category}'

    class Meta:
        verbose_name_plural = 'Categories'


class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'Driver: {self.first_name} {self.last_name}'


class Transport(models.Model):
    number = models.CharField(max_length=10, unique = True)
    model = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    required_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver)

    def __str__(self):
        return f'Transport: {self.model} {self.number}'

