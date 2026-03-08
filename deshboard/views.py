from django.db.models import Sum
from django.db.models.functions import TruncMonth
from rest_framework.views import APIView
from rest_framework.response import Response
from Transaction.models import TansactionModel

class SummaryView(APIView):
    def get(self, request):
        income = TansactionModel.objects.filter(types='income').aggregate(
            total=Sum('amount')
        )['total'] or 0
        expense = TansactionModel.objects.filter(types='expense').aggregate(
            total=Sum('amount')
        )['total'] or 0
        balance = income - expense
        return Response({
            "total_income": income,
            "total_expense": expense,
            "balance": balance
        })
    
class MonthlyView(APIView):
    def get(self, request):
        data = (
            TansactionModel.objects
            .annotate(month=TruncMonth('date'))
            .values('month', 'types')
            .annotate(total=Sum('amount'))
            .order_by('month')
        )
        result = {}
        for item in data:
            month = item['month'].strftime('%Y-%m')
            if month not in result:
                result[month] = {"income": 0, "expense": 0}
            result[month][item['types']] = item['total']
        response = [
            {"month": k, "income": v["income"], "expense": v["expense"]}
            for k, v in result.items()
        ]
        return Response(response)
    
class CategorySummaryView(APIView):
    def get(self, request):
        data = (
            TansactionModel.objects
            .filter(types='expense')
            .values('category__name')
            .annotate(total=Sum('amount'))
        )
        response = [
            {
                "category": item['category__name'],
                "total": item['total']
            }
            for item in data
        ]
        return Response(response)