"""sentiment_twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from rest_framework.views import APIView
from rest_framework.response import Response
from PriceFetcher import getThreeYearClosingPrices


class StockData(APIView):
    def get(self, request):
        symbol = request.query_params.get('name', None)
        data = getThreeYearClosingPrices(symbol)
        return Response(data)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pricedata/', StockData.as_view()),
]
