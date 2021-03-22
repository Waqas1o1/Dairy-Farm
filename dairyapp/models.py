from django.db import models
from django.utils import timezone
from dairyapp.choices import MILK_CHOICES
import datetime

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Milk Product Units


class mProductUnit(models.Model):
    mProductUnit_id = models.AutoField(primary_key=True)
    mProductUnit_name = models.CharField(max_length=10)

    def __str__(self):
        return self.mProductUnit_name


# Milk Products


class mProduct(models.Model):
    # KILOGRAM='kg.'
    # LITER='ltr'
    # PACKET='pkt'
    #
    # MILK_PRODUCTS_UNIT_CHOICES=(
    #     (KILOGRAM,'Kilogram'),
    #     (LITER,'Liter'),
    #     (PACKET,'Packet'),
    # )

    mProduct_id = models.AutoField(primary_key=True)
    mProduct_name = models.CharField(max_length=50)

    # Product Unit has one to many relationship with mProduct
    mProduct_qtyunit = models.ForeignKey(
        mProductUnit, on_delete=models.CASCADE)
    mProduct_qty = models.FloatField(default=0)  # current stock
    # mProduct_qtyunit=models.CharField(max_length=3,choices=MILK_PRODUCTS_UNIT_CHOICES,default=LITER)  ##unit type eg. ltr, kg, ml

    def __str__(self):
        return self.mProduct_name
# Animal Details


class animalDetail(models.Model):
    animalDetail_id = models.AutoField(primary_key=True)
    animalDetail_name = models.CharField(max_length=50, unique=True)
    animalDetail_product = models.ForeignKey(
        mProduct, on_delete=models.CASCADE)
    animalDetail_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.animalDetail_name = self.animalDetail_name.upper()
        super(animalDetail, self).save(*args, **kwargs)

    def __str__(self):
        return self.animalDetail_name

# milk purchase


class mPurchase(models.Model):

    mPurchase_id = models.AutoField(primary_key=True)
    seller = models.CharField(max_length=50)
    mPurchase_date = models.DateField(blank=True, null=True)
    mPurchase_product = models.CharField(max_length=15, choices=MILK_CHOICES)
    mPurchase_qty = models.FloatField()
    mPurchase_rate = models.FloatField()
    mPurchase_total = models.FloatField(default=0)

    def __str__(self):
        return self.seller

# Dairy Stock Add


class mStock(models.Model):
    mStock_id = models.AutoField(primary_key=True)
    mStock_date = models.DateTimeField(
        default=timezone.now)
    mStock_time = models.TimeField(default=timezone.now)
    mStock_product = models.ForeignKey(mProduct, on_delete=models.CASCADE)
    mStock_product_detail = models.CharField(max_length=50)
    mStock_qty = models.FloatField()

    def __str__(self):
        return self.mStock_product_detail
    # try to access unit using mProduct.mProduct_qtyunit
    # not sure here if it works !!
    # check and verify it later

    def save(self, *args, **kwargs):
        self.mStock_product_detail = self.mStock_product_detail.upper()
        super(mStock, self).save(*args, **kwargs)

# milk product sell


class mProductSell(models.Model):
    mProductSell_id = models.AutoField(primary_key=True)
    buyer_name = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    milk_product = models.ForeignKey(
        mProduct, on_delete=models.SET_NULL, null=True)
    # automatically set the field to now when the object is created
    mProductSell_date = models.DateField(
        blank=True, null=True, default=datetime.date.today)
    Payment_Method = [
        ('Cash', 'Cash'),
        ('Credit', 'Credit'),
    ]
    mProductSell_paymentMethod = models.CharField(
        choices=Payment_Method, max_length=10, default='Cash')
    mProductSell_qty = models.FloatField()
    mProductSell_qtyunit = models.CharField(max_length=10, default='TBD')
    mProductSell_rate = models.FloatField()
    mProductSell_amount = models.FloatField(default=0)

    def __str__(self):
        return self.buyer_name.name


class operationCost(models.Model):
    operationCost_id = models.AutoField(primary_key=True)
    particular = models.CharField(max_length=80)
    date = models.DateField(blank=True, null=True, default=datetime.date.today)
    qty = models.FloatField()
    rate = models.FloatField()
    amount = models.FloatField()

    def __str__(self):
        return self.particular

# Assets


class Assets(models.Model):
    assets_id = models.AutoField(primary_key=True)
    particular = models.CharField(max_length=80)
    date = models.DateField(blank=True, null=True, default=datetime.date.today)
    qty = models.FloatField()
    rate = models.FloatField()
    amount = models.FloatField()

    def __str__(self):
        return self.particular

# Expensives


class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    particular = models.CharField(max_length=80)
    date = models.DateField(blank=True, null=True, default=datetime.date.today)
    qty = models.FloatField()
    rate = models.FloatField()
    amount = models.FloatField()

    def __str__(self):
        return self.particular


class test(models.Model):
    test_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


# Customer Chart Flow
class customerLedger(models.Model):
    sell_invoice = models.ForeignKey(mProductSell, on_delete=models.CASCADE)
    payment_recived = models.FloatField()

    def __str__(self, *args, **kwargs):
        return str(self.sell_invoice.buyer_name)

    def save(self, *args, **kwargs):
        if (self.sell_invoice.mProductSell_paymentMethod == 'Credit'):
            self.payment_recived = 0
        else:
            self.payment_recived = self.sell_invoice.mProductSell_amount
        super(customerLedger, self).save(*args, **kwargs)
