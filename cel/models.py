from django.db import models
from django_filters import FilterSet, CharFilter, BaseInFilter


# python manage.py migrate --fake cel zero
# python manage.py migrate cel
class NewsModel(models.Model):
    title = models.CharField(max_length=100, null=False, primary_key=True, blank=False)
    intensity = models.IntegerField(null=True, blank=False)
    likelihood = models.IntegerField(null=True, blank=False)
    relevance = models.IntegerField(null=True, blank=False)
    published = models.DateField(null=True, blank=True)

    # filterable
    pestle = models.CharField(max_length=100, null=True, blank=False)
    end_year = models.IntegerField(null=True, blank=False)
    topic = models.CharField(max_length=100, null=True, blank=False)
    region = models.CharField(max_length=100, null=True, blank=False)
    source = models.CharField(null=True, blank=False, max_length=100)
    sector = models.CharField(max_length=50, null=True, blank=False)
    country = models.CharField(max_length=100, null=True, blank=False)


class CharInFilter(BaseInFilter, CharFilter):
    pass


class NewsFilter(FilterSet):
    # pestle = CharFilter(lookup_expr='iexact')
    pestle = CharInFilter()
    source = CharInFilter()
    end_year = CharInFilter()
    topic = CharInFilter()
    region = CharInFilter()
    sector = CharInFilter()
    country = CharInFilter()

    # username = CharFilter(method='my_custom_filter')
    '''
    skipped `Meta` for dynamic query
    '''
    # class Meta:
    #     model = NewsModel
        # fields = ['pestle']
        # fields = {
        #     'pestle': ["in", "exact"],
        # }
