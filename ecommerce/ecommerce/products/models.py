from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey

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
    categories = models.ManyToManyField(Category, related_name='categories')
    # ................................................................ #
    created_at = models.DateTimeField(auto_now_add=True)
    # ................................................................ #
    updated_at = models.DateTimeField(auto_now = True)
    # ................................................................ #
    featured_image = models.ImageField(verbose_name=_('Image'),
                              help_text=_('uplaod a featured image'),
                              upload_to='products/images/',
                              default='products/images/img1.png')
    # ................................................................ #
    alt_text = models.CharField(verbose_name=_('Alternative text'),
                                help_text=_('Please add a alternative text'),
                                max_length=255,
                                null=True,
                                blank=True)
    # ................................................................ #

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title

    def get_price(self, *arg, **kwargs):
        return self.regular_price

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
                              upload_to='products/images/',
                              default='products/images/img1.png')
    # ................................................................ #
    alt_text = models.CharField(verbose_name=_('Alternative text'),
                                help_text=_('Please add a alternative text'),
                                max_length=255,
                                null=True,
                                blank=True)
    # ................................................................ #
    created_at = models.DateTimeField(auto_now_add=True)
    # ................................................................ #
    updated_at = models.DateTimeField(auto_now = True)
    # ................................................................ #

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
# ==================================================================== #


