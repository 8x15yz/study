from .models import Trade
from .serializers import TradeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def trade_list(request):
    if request.method == 'GET':
        trade = Trade.objects.all()
        serializer = TradeSerializer(trade, many=True)
        return Response(serializer.data)