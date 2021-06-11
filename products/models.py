from django.db import models

# Create your models here.


class Brand(models.Model):
    class Meta:
        db_table = 'brands'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    title = models.CharField(null=False, blank=False, max_length=200, verbose_name='Title')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Product(models.Model):
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    # category = models.ForeignKey(Category)
    title = models.CharField(null=False, blank=False, max_length=200, verbose_name='Title')
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2, null=False, blank=False, verbose_name='Price')
    old_price = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True, verbose_name='Old price')
    quantity = models.IntegerField(default=1, null=False, blank=False, verbose_name='Quantity')
    photo = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Photo')
    brand = models.ForeignKey(Brand, related_name='products', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Brand')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(null=False, blank=False, max_length=200, verbose_name='Title')
    is_active = models.BooleanField(null=False, blank=False, default=True, verbose_name='Активна')

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    class Meta:
        db_table = 'products_categories'
        verbose_name = 'Product to category'
        verbose_name_plural = 'Products to categories'

    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Product')
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Category')


class ProductReview(models.Model):
    class Meta:
        db_table = 'products_reviews'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    product = models.ForeignKey(Product, related_name='reviews', null=False, blank=False, on_delete=models.CASCADE, verbose_name='Product')
    review = models.TextField(null=False, blank=False, verbose_name='Review')



