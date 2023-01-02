from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey

# from django.contrib.auth.models import User - deprecated, new custom user model needed for Product.created_by

# ==================================================================== #
class Category(MPTTModel):
    """
    Category table implemented with MPTT.
    """
    # ................................................................ #
    name = models.CharField(verbose_name=_('Category Name'),
                            help_text=_('Required and unique'),
                            max_length=255,
                            unique=True)
    # ................................................................ #
    slug = models.SlugField(verbose_name=_('Category safe url'),
                            max_length=255,
                            unique=True)
    # ................................................................ #
    parent = TreeForeignKey('self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            related_name='children')
    # ................................................................ #
    is_active = models.BooleanField(default=True)
    # ................................................................ #

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


# ==================================================================== #
class ProductType(models.Model):
    """
    ProductType table will provide list of all products for sale
    """
    # ................................................................ #
    name = models.CharField(verbose_name=_('Product Name'),
                            max_length=255,
                            help_text=_('Required'),
                            unique=True)
    # ................................................................ #
    is_active = models.BooleanField(default = True)
    # ................................................................ #

    class Meta:
        verbose_name = _('Product Type')
        verbose_name_plural = _('Product Types')

    def __str__(self):
        return self.name

# ==================================================================== #
class ProductSpecification(models.Model):
    """
    ProductSpecification table will provide list of product specifications
    or features for the product types (ProductType)
    """
    # ................................................................ #
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    # ................................................................ #
    name = models.CharField(verbose_name=_('Name'),
                             help_text='Required',
                             max_length=255)
    # ................................................................ #

    class Meta:
        verbose_name = _('Product Specification')
        verbose_name_plural = _('Product Specifications')

    def __str__(self):
        return self.name

# ==================================================================== #
class Product(models.Model):
    """
    The product table contianing all the product items.
    """
    # ................................................................ #
    title = models.CharField(verbose_name=_('Title'),
                             help_text=_('Required'),
                             max_length=255)
    # ................................................................ #
    description = models.TextField(verbose_name=_('Description'),
                                   help_text=_('Not Required'),
                                   blank=True)
    # ................................................................ #
    slug = models.SlugField(max_length=255)
    # ................................................................ #
    regular_price = models.DecimalField(verbose_name=_('Regular Price'),
                                        help_text=_('Max 999.99'),
                                        max_digits=5,
                                        decimal_places=2,
                                        error_messages={
                                            'name': {
                                                'max_length': _('The price must be between 0 and 999.99.')
                                            }
                                        })
    # ................................................................ #
    discout_price = models.DecimalField(verbose_name=_('Discount Price'),
                                        help_text=_('Max 999.99'),
                                        max_digits=5,
                                        decimal_places=2,
                                        error_messages={
                                            'name': {
                                                'max_length': _('The price must be between 0 and 999.99.')
                                            }
                                        })
    # ................................................................ #
    is_active = models.BooleanField(verbose_name=_('Product Visibility'),
                                    help_text=_('Change product visibility'),
                                    default=True)
    # ................................................................ #
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    # ................................................................ #
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    # ................................................................ #
    users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                            related_name='user_wishlist',
                                            blank=True)
    # ................................................................ #
    created_at = models.DateTimeField(auto_now_add=True)
    # ................................................................ #
    updated_at = models.DateTimeField(auto_now = True)
    # ................................................................ #

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title

# ==================================================================== #
class ProductSpecificationValue(models.Model):
    """
    ProductSpecificationValue table holds each of the
    products individual specification or bespoke features
    """
    # ................................................................ #
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # ................................................................ #
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    # ................................................................ #
    value = models.CharField(verbose_name=_('value'),
                             help_text=_('Product specification value (max 255 words)'),
                             max_length=255)
    # ................................................................ #

    class Meta:
        verbose_name = _('Product Specification Value')
        verbose_name_plural = _('Product Specification Values')

    def __int__(self):
        return self.value

# ==================================================================== #
class ProductImage(models.Model):
    """
    The product image table contianing all the product images.
    """
    # ................................................................ #
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='product_image')  # The related name is for the template reference.
    # ................................................................ #
    image = models.ImageField(verbose_name=_('Image'),
                              help_text=_('uplaod a product image'),
                              upload_to='images/',
                              default='images/img1.png')
    # ................................................................ #
    alt_text = models.CharField(verbose_name=_('Alternative text'),
                                help_text=_('Please add a alternative text'),
                                max_length=255,
                                null=True,
                                blank=True)
    # ................................................................ #
    is_feature = models.BooleanField(default=False)
    # ................................................................ #
    created_at = models.DateTimeField(auto_now_add=True)
    # ................................................................ #
    updated_at = models.DateTimeField(auto_now = True)
    # ................................................................ #

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
# ==================================================================== #


















