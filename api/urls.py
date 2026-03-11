from rest_framework.routers import DefaultRouter
#from account.views import AuthViewSet
from Transaction.views import TransactionView
from Category.views import CateloryView
from deshboard.views import SummaryView, CategorySummaryView, MonthlyView
from django.urls import path, include

router = DefaultRouter()
#router.register('auth', AuthViewSet, basename='auth')
#router.register('category', )
router.register('transaction', TransactionView, basename= 'tran')
router.register('category', CateloryView, basename='category')


urlpatterns = router.urls

urlpatterns = [
    path('deshboard/', include('deshboard.urls')),
]
