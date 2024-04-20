# from django.core.exceptions import ValidationError
from django.db import models
# from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings

class contactModel(models.Model):
    name = models.CharField(max_length=70, blank=False, null=False,
                            help_text=_("Required. The surname or lastname."))
    email = models.EmailField(help_text=_("Enter your email here. e.g: name@gmail.com."))
    subject = models.CharField(max_length=100, blank=False, null=False, help_text=_("Required subject from you."))
    message = models.TextField(blank=True, null=True,
                               help_text=_("Required message from you."))

    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "contact"
        verbose_name = "contact"
        verbose_name_plural = "contacts"

class customerModel(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "customer"
        verbose_name = "customer"
        verbose_name_plural = "customers"

def get_upload_path(instance, filename):
    model = instance.album.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/product_img/{filename}'

class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()
    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)

class imagesModel(models.Model):
    # images = models.FileField(upload_to="product/")
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=get_upload_path)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)

    class Meta:
        db_table = "image"
        verbose_name = "image"
        verbose_name_plural = "images"
class productModel(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    album = models.ManyToManyField(ImageAlbum, related_name='model')
    digital = models.BooleanField(default=False, null=True, blank=True)
    detail = models.CharField(max_length=300, null=True)
    # likes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='myapp.Like')
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        verbose_name = "product"
        verbose_name_plural = "products"

# class Like(models.Model):
#   time = models.DateTimeField(auto_now_add=True)
#   post = models.ForeignKey(productModel, on_delete=models.CASCADE)
#   user = models.ForeignKey(User, on_delete=models.CASCADE)

# class sizeModel(models.Model):
#     SizeChoices = (
#         ("XL", "XL"),
#         ("XXL", "XXL"),
#         ("sm", "Small"),
#         ("md", "Medium"),
#         ("lg", "Large"),
#     )
#     size = models.CharField(max_length=20, choices=SizeChoices, default="XL", help_text=_("Choose one of the sizes that you fit!"))


class orderModel(models.Model):
    customer = models.ForeignKey(customerModel, on_delete=models.SET_NULL, null=True, blank=True, related_name="order")
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "order"
        verbose_name = "order"
        verbose_name_plural = "orders"


class cartModel(models.Model):
    product = models.ForeignKey(productModel, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name="cart_product")
    order = models.ForeignKey(orderModel, on_delete=models.SET_NULL, null=True, blank=True, related_name="cart_order")
    # p_size = models.ForeignKey(sizeModel, on_delete=models.SET_NULL, null=True, help_text=_("Choose a size."),
    #                                                               related_name='p_size')
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "cart"
        verbose_name = "cart"
        verbose_name_plural = "carts"


class shippingaddressModel(models.Model):
    customer = models.ForeignKey(productModel, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name="shadd_product")
    order = models.ForeignKey(orderModel, on_delete=models.SET_NULL, null=True, blank=True, related_name="shadd_order")
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        db_table = "shippingaddress"
        verbose_name = "shippingaddress"
        verbose_name_plural = "shippingaddresses"

