from django import forms
from .models import mProduct, mProductUnit, mPurchase, mStock, mProductSell, operationCost, test, animalDetail, Assets, Purchase, Customer
from dairyapp.choices import MILK_CHOICES
import datetime
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class mPurchaseForm(forms.ModelForm):
    """
        This form is for milk purchase
    """

    seller = forms.CharField(
        label='Seller Name | بیچنے والے کا نام',
        max_length=50,
        help_text="Please Enter Seller Name",
    )

    mPurchase_date = forms.DateField(
        label='Date | تاریخ',
        # input_formats=['%Y-%m-%d'],
    )

    mPurchase_product = forms.ChoiceField(
        choices=MILK_CHOICES,
        label='Milk Type | دودھ کی قسم',
        initial='',
        widget=forms.Select(),
        help_text="Choose milk type from options",
        required=True
    )

    mPurchase_qty = forms.FloatField(
        label='Qty | مقدار',
        help_text="The quantity must be in numeric format",

    )

    mPurchase_rate = forms.FloatField(
        label='Rate/Ltr | شرح',
        help_text="The rate should be in numeric format",

    )

    def __init__(self, *args, **kwargs):
        super(mPurchaseForm, self).__init__(*args, **kwargs)
        self.fields['mPurchase_date'].widget.attrs['id'] = 'nepalicalendar'

    class Meta:
        model = mPurchase
        fields = ('seller', 'mPurchase_date', 'mPurchase_product',
                  'mPurchase_qty', 'mPurchase_rate',)

    # Negative Value Validations
    def clean(self):
        super(mPurchaseForm, self).clean()
        mPurchase_date = self.cleaned_data.get('mPurchase_date')
        mPurchase_qty = self.cleaned_data.get('mPurchase_qty')
        mPurchase_rate = self.cleaned_data.get('mPurchase_rate')

        try:
            datetime.datetime.strptime(str(mPurchase_date), '%Y-%m-%d')
        except ValueError:
            self._errors['mPurchase_date'] = self.error_class(
                ["Date should be in YYYY-mm-dd format"])

        if(mPurchase_qty < 0):
            self._errors['mPurchase_qty'] = self.error_class(
                ["Negative value not allowed"])

        if(mPurchase_rate < 0):
            self._errors['mPurchase_rate'] = self.error_class(
                ["Negative value not allowed"])

        return self.cleaned_data


class mStockForm(forms.ModelForm):
    """
        This form is for adding milk product stock
    """
    mStock_product = forms.ModelChoiceField(
        queryset=mProduct.objects.filter(),
        label='Select Milk Product',
        help_text="Choose from the list of milk products",
        required=True,
        widget=forms.Select(attrs={'onChange': 'refrash()'})
    )

    mStock_date = forms.DateField(
        label='Date',
        required=True,
    )
    mStock_qty = forms.FloatField(
        label='Quantity',
        help_text='Enter stock quantity',
        required=True,
    )
    Animal_type = [
        ("COW-101", "COW-101"),
    ]

    mStock_product_detail = forms.ModelChoiceField(
        label='Product detail',
        queryset=animalDetail.objects.all()

    )

    def __init__(self, *args, **kwargs):
        super(mStockForm, self).__init__(*args, **kwargs)
        self.fields['mStock_date'].widget.attrs['id'] = 'nepalicalendar'

    def clean(self):
        super(mStockForm, self).clean()
        mStock_date = self.cleaned_data.get('mStock_date')
        mStock_qty = self.cleaned_data.get('mStock_qty')
        mStock_product_detail = self.cleaned_data.get('mStock_product_detail')

        try:
            datetime.datetime.strptime(str(mStock_date), '%Y-%m-%d')
        except ValueError:
            self._errors['mStock_date'] = self.error_class(
                ["Date should be in YYYY-mm-dd format"])

        # Negative Value Validations
        if (mStock_qty < 0):
            self._errors['mStock_qty'] = self.error_class(
                ["Negative value not allowed"])

        return self.cleaned_data

    class Meta:
        model = mStock
        fields = ('mStock_product', 'mStock_date',
                  'mStock_qty', 'mStock_product_detail')


class mProductSellForm(forms.ModelForm):
    """
        This form is for selling products
    """

    buyer_name = forms.ModelChoiceField(
        label='Buyer Name | خریدار نام',
        queryset=Customer.objects.all(),
        help_text="Please Enter Buyer Name/Select From Dropdown",
        required=True,
    )

    milk_product = forms.ModelChoiceField(
        queryset=mProduct.objects.filter(),
        label='Select Milk Product',
        help_text="Choose from the list of milk products | دودھ کی مصنوعات کو منتخب کریں",
        required=True
    )

    mProductSell_date = forms.DateField(
        label='Date',
        required=True,
    )

    mProductSell_paymentMethod = forms.ChoiceField(
        choices=(('Cash', 'Cash'), ('Credit', 'Credit')),
        label='Payment Method'
    )

    mProductSell_qty = forms.FloatField(
        label='Quantity | مقدار',
        help_text='Enter product quantity',
        required=True,
    )

    mProductSell_rate = forms.FloatField(
        label='Rate | شرح',
        help_text='Enter product rate',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(mProductSellForm, self).__init__(*args, **kwargs)
        self.fields['mProductSell_date'].widget.attrs['id'] = 'nepalicalendar'

    def clean(self):
        super(mProductSellForm, self).clean()
        mProductSell_date = self.cleaned_data.get('mProductSell_date')
        mProductSell_qty = self.cleaned_data.get('mProductSell_qty')
        mProductSell_rate = self.cleaned_data.get('mProductSell_rate')
        mProductSell_paymentMethod = self.cleaned_data.get(
            'mProductSell_paymentMethod')
        try:
            datetime.datetime.strptime(str(mProductSell_date), '%Y-%m-%d')
        except ValueError:
            self._errors['mProductSell_date'] = self.error_class(
                ["Date should be in YYYY-mm-dd format"])

        # Negative Value Validations
        if (mProductSell_qty < 0):
            self._errors['mProductSell_qty'] = self.error_class(
                ["Negative value not allowed"])

        if (mProductSell_rate < 0):
            self._errors['mProductSell_rate'] = self.error_class(
                ["Negative value not allowed"])

        return self.cleaned_data

    class Meta:
        model = mProductSell
        fields = ('buyer_name', 'milk_product', 'mProductSell_date',
                  'mProductSell_qty', 'mProductSell_rate', 'mProductSell_paymentMethod')


# operation cost form
class operationCostForm(forms.ModelForm):
    """
        This form is for operational costs!
    """

    particular = forms.CharField(
        label='Particular |  خاص',
        required=True,
    )
    date = forms.DateField(
        label='Date | تاریخ',
        required=True,
    )

    qty = forms.FloatField(
        label='Quantity | مقدار',
        help_text='Enter Quantity | مقدار',
        required=True,
    )

    rate = forms.FloatField(
        label='Rate شرح| ',
        help_text='Enter Rate | شرح',
        required=True,
    )

    class Meta:
        model = operationCost
        fields = ('particular', 'date', 'qty', 'rate')

    def __init__(self, *args, **kwargs):
        super(operationCostForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['id'] = 'nepalicalendar'

    def clean(self):
        super(operationCostForm, self).clean()
        date = self.cleaned_data.get('date')
        qty = self.cleaned_data.get('qty')
        rate = self.cleaned_data.get('rate')

        # date validation
        try:
            datetime.datetime.strptime(str(date), '%Y-%m-%d')
        except ValueError:
            self._errors['date'] = self.error_class(
                ["Date should be in YYYY-mm-dd format"])

        # Negative Value Validation
        if(qty < 0):
            self._errors['qty'] = self.error_class(
                ["Negative value not allowed"])

        if(rate < 0):
            self._errors['rate'] = self.error_class(
                ["Negative value not allowed"])

        return self.cleaned_data


class AssetesForm(forms.ModelForm):
    """
        This form is for  assets!
    """

    particular = forms.CharField(
        label='Particular |  خاص',
        required=True,
    )
    date = forms.DateField(
        label='Date | تاریخ',
        required=True,
    )

    qty = forms.FloatField(
        label='Quantity | مقدار',
        help_text='Enter Quantity | مقدار',
        required=True,
    )

    rate = forms.FloatField(
        label='Rate شرح| ',
        help_text='Enter Rate | شرح',
        required=True,
    )

    class Meta:
        model = Assets
        fields = ('particular', 'date', 'qty', 'rate')

    def __init__(self, *args, **kwargs):
        super(AssetesForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['id'] = 'nepalicalendar'

    def clean(self):
        super(AssetesForm, self).clean()
        date = self.cleaned_data.get('date')
        qty = self.cleaned_data.get('qty')
        rate = self.cleaned_data.get('rate')

        # date validation
        try:
            datetime.datetime.strptime(str(date), '%Y-%m-%d')
        except ValueError:
            self._errors['date'] = self.error_class(
                ["Date should be in YYYY-mm-dd format"])

        # Negative Value Validation
        if(qty < 0):
            self._errors['qty'] = self.error_class(
                ["Negative value not allowed"])

        if(rate < 0):
            self._errors['rate'] = self.error_class(
                ["Negative value not allowed"])

        return self.cleaned_data


class PurchasesForm(forms.ModelForm):
    """
        This form is for  Purchases!
    """

    particular = forms.CharField(
        label='Particular |  خاص',
        required=True,
    )
    date = forms.DateField(
        label='Date | تاریخ',
        required=True,
    )

    qty = forms.FloatField(
        label='Quantity | مقدار',
        help_text='Enter Quantity | مقدار',
        required=True,
    )

    rate = forms.FloatField(
        label='Rate شرح| ',
        help_text='Enter Rate | شرح',
        required=True,
    )

    class Meta:
        model = Purchase
        fields = ('particular', 'date', 'qty', 'rate')

    def __init__(self, *args, **kwargs):
        super(PurchasesForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['id'] = 'nepalicalendar'

    def clean(self):
        super(PurchasesForm, self).clean()
        date = self.cleaned_data.get('date')
        qty = self.cleaned_data.get('qty')
        rate = self.cleaned_data.get('rate')

        # date validation
        try:
            datetime.datetime.strptime(str(date), '%Y-%m-%d')
        except ValueError:
            self._errors['date'] = self.error_class(
                ["Date should be in YYYY-mm-dd format"])

        # Negative Value Validation
        if(qty < 0):
            self._errors['qty'] = self.error_class(
                ["Negative value not allowed"])

        if(rate < 0):
            self._errors['rate'] = self.error_class(
                ["Negative value not allowed"])

        return self.cleaned_data

# nepali date selection form


class dateForm(forms.Form):

    fromdate = forms.DateField(
        label='FROM',

    )

    todate = forms.DateField(
        label='TO',
    )

    def __init__(self, *args, **kwargs):
        super(dateForm, self).__init__(*args, **kwargs)
        self.fields['fromdate'].widget.attrs['id'] = 'nepalicalendar'
        self.fields['todate'].widget.attrs['id'] = 'nepalicalendar2'

    # validate and clean entered date value
    def clean(self):
        super(dateForm, self).clean()
        fromdate = self.cleaned_data.get('fromdate')
        todate = self.cleaned_data.get('todate')

        try:
            datetime.datetime.strptime(str(fromdate), '%Y-%m-%d')
        except ValueError:
            self._errors['fromdate'] = self.error_class(
                ["Date should be in YYYY-mm-dd format"])

        try:
            datetime.datetime.strptime(str(todate), '%Y-%m-%d')
        except ValueError:
            self._errors['todate'] = self.error_class(
                ["Date should be in YYYY-mm-dd format"])

    class Meta:
        fields = ('fromdate', 'todate')


# popup forms for settings

class addCustomerForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    name = forms.CharField(
        label='Product Name',
        max_length=30
    )

    address = forms.CharField(
        label='Customer Address',
        max_length=100
    )
    contact = forms.CharField(
        label='Customer Contact',
        max_length=11,
        min_length=11,
        required=True
    )

    class Meta:
        model = mProduct
        fields = ['name', 'address', 'contact']


class addProductForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    mProduct_name = forms.CharField(
        label='Product Name'
    )

    mProduct_qtyunit = forms.ModelChoiceField(
        label='Select Unit Type',
        queryset=mProductUnit.objects.filter(),
    )

    class Meta:
        model = mProduct
        fields = ['mProduct_name', 'mProduct_qtyunit']

# add /create product unit form


class addProductUnitForm(forms.ModelForm):
    mProductUnit_name = forms.CharField(
        label='Product Unit Name | پروڈکٹ یونٹ کا نام'
    )

    class Meta:
        model = mProductUnit
        fields = ['mProductUnit_name']

# Animal Details


class addAnimaldetailForm(forms.ModelForm):
    animalDetail_name = forms.CharField(
        label='Animal Details'
    )
    animalDetail_product = forms.ModelChoiceField(
        queryset=mProduct   .objects.all(),
        label='Select Product',
        required=True,
        help_text='Select Relevant Animal Product'
    )

    class Meta:
        model = animalDetail
        fields = ['animalDetail_name', 'animalDetail_product']
# test form


class testForm(forms.ModelForm):
    name = forms.CharField(
        label='name'
    )
    date = forms.DateTimeField(
        label='date'
    )

    def __init__(self, *args, **kwargs):
        super(testForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['id'] = 'nepalicalendar'

    # validate and clean entered date value
    def clean(self):
        super(testForm, self).clean()
        date = self.cleaned_data.get('date')

    class Meta:
        model = test
        fields = ('name', 'date',)
