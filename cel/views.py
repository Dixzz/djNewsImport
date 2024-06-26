from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from .models import NewsModel, NewsFilter
# from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes

import django_filters


# celery -A foo worker -l info -E --pool=solo


class MySerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    startDate = serializers.DateField()
    endDate = serializers.DateField()


@api_view(['GET'])
@csrf_exempt
# @renderer_classes((JSONRenderer))
def getNewsFilters(request):
    qs = NewsModel.objects.values("pestle").distinct().filter(pestle__isnull=False).exclude(pestle__exact='')
    return Response({'count': qs.count()}, status=200)
    
@api_view(['POST'])
@csrf_exempt
# @renderer_classes((JSONRenderer))
def getNews(request):
    # serializer = MySerializer(data=request.data)
    # print(serializer.is_valid())

    inp = request.data
    print(f'inp is: {inp}, inp type: {type(inp)}')
    qs = NewsFilter(inp, queryset=NewsModel.objects.all())
    return Response({'count': qs.qs.count()}, status=200)

    # print(foo.delay('hey...'))
    # AlertMasterModel.objects.filter(userId=pk.id, generated_time__range=(startDate, endDate))
    # print(AlertMasterModel.objects.all())
    # print(AlertMasterModel.objects.using('aml').all())
