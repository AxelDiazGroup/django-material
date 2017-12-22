from django.utils.translation import ugettext_lazy as _
from material.views import ModelViewSet

from . import models


class CityViewset(ModelViewSet):
    model = models.City
    list_columns = ('name', 'country', 'population')


class ContinentViewset(ModelViewSet):
    model = models.Continent
    list_columns = (
        'name', 'surrounded_oceans', 'countries_count',
        'area', 'population',
    )

    def surrounded_oceans(self, contintent):
        return ', '.join(ocean.name for ocean in contintent.oceans.all())
    surrounded_oceans.short_description = _('Surrounded oceans')


class CountryViewset(ModelViewSet):
    model = models.Country
    list_columns = (
        'tld', 'name', 'continent',
        'became_independent_in_20_century',
        'gay_friendly'
    )

    def tld(self, country):
        return '.' + country.code.lower()
    tld.short_description = 'TLD'

    def became_independent_in_20_century(self, country):
        if country.independence_day:
            return 1900 <= country.independence_day.year <= 2000
    became_independent_in_20_century.short_description = _('Became independent in XX century')


class OceanViewset(ModelViewSet):
    model = models.Ocean
    list_columns = ('name', 'area', )


class SeaViewset(ModelViewSet):
    model = models.Sea
    list_columns = ('name', 'parent', 'ocean', 'sea_area', )

    def sea_area(self, sea):
        return None if sea.area == 0 else sea.area
