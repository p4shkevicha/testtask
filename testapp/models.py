from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Manufacturer name',
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation date',
    )

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

    def __str__(self):
        return self.name


class Contract(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Contract title',
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation date',
    )

    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'

    def __str__(self):
        return self.title

    @property
    def manufacturers_id(self):
        return sorted(
            LoanApplication.objects.filter(
                contract__id=self.id,
            )
            .values_list('product__manufacturer', flat=True)
            .distinct(),
        )


class LoanApplication(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Loan application title',
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation date',
    )
    contract = models.ForeignKey(
        to=Contract,
        on_delete=models.PROTECT,
        related_name='loan_application',
        verbose_name='Contract',
    )

    class Meta:
        verbose_name = 'Loan application'
        verbose_name_plural = 'Loan applications'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Product name',
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation date',
    )
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.PROTECT,
        related_name='product',
        verbose_name='Manufacturer',
    )
    loan_application = models.ForeignKey(
        to=LoanApplication,
        on_delete=models.SET_NULL,
        related_name='product',
        verbose_name='Loan application',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
