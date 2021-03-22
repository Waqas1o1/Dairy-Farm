from django.urls import path, include
from . import views

app_name = 'dairyapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('autocomplete/<int:pdt>', views.getProduct, name='get-product'),
    path('milkpurchase/', views.milkPurchase, name='milk-purchase'),
    path('milkpurchase/<id>/delete',
         views.milkPurchaseDelete, name='delete-purchase'),
    path('addmilkproducts/', views.addMilkProducts, name='add-milk-products'),
    path('sellmilkproducts/', views.sellMilkProducts, name='sell-milk-products'),
    path('sellmilkproducts/<id>/delete',
         views.mProductSellDelete, name='delete-sales'),
    path('stockrecords/<id>', views.mStockDetailView, name='stock-detail'),
    path('stockAniamlrecords/<str:d>', views.mStockAnimalDetailView,
         name='stock-Animal-detail'),
    path('operationcost/', views.operationCost, name='operation-cost'),
    path('Assets/', views.Asset, name='assets-cost'),
    path('Purchases/', views.Purchases, name='purchases-cost'),

    path('operationcost/<id>/delete', views.deleteOperationCost,
         name='delete-operation-cost'),
    path('assets/<id>/delete', views.deleteAsset,
         name='delete-asset'),
    path('purchase/<id>/delete', views.deletePurchase,
         name='delete-purchase'),


    path('report/', views.report, name='report'),
    path('report/purchasereport/', views.purchaseReport, name='purchase-report'),
    path('report/stockreport/', views.stockReport, name='stock-report'),
    path('report/customerladgerreport/',
         views.CustoemrLagderReport, name='ladger-report'),
    path('report/salesreport/', views.salesReport, name='sales-report'),
    path('report/operationcostreport',
         views.operationCostReport, name='operationcost-report'),
    path('report/assetsreport',
         views.AssetsReport, name='assets-report'),
    path('report/purchasesreport',
         views.PurchasesReport, name='purchases-report'),
    path('settings/', views.settings, name='settings'),
    path('settings/createproduct',
         views.newProductCreateView.as_view(), name='create-product'),
    path('settings/addCustomer',
         views.newCutomerAddView.as_view(), name='add-customer'),
    path('settings/createAnimalDetails',
         views.newAnimalCreateView, name='create-animal-detail'),
    path('settings/createproductunit',
         views.newProductUnitCreate, name='create-product-unit'),
    path('test/', views.test, name='test'),
    # path('stockrecords/<id>/delete',views.mStockRecordDelete,name='delete-stock-records'),

]
