from django.shortcuts import render
import pandas as pd
from rest_framework import viewsets
from wineApp.models import Wine
#from .utils import loadData
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import serializers
import numpy as np

class WineAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wine
        fields = ('country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2', 'variety', 'winery')


class GetData(viewsets.ModelViewSet):
    queryset = Wine.objects.all()
    serializer_class = WineAppSerializer


class Filtered(generics.ListAPIView):
    serializer_class = WineAppSerializer

    def get_queryset(self):
        country = self.request.query_params.get('country', None)
        province = self.request.query_params.get('province', None)
        region_1 = self.request.query_params.get('region_1', None)
        region_2 = self.request.query_params.get('region_2', None)
        sort_order = self.request.query_params.get('sort_order', None)

        queryset = Wine.objects.all()
        if country is not None:
            queryset = queryset.filter(country__icontains=country)
        if province is not None:
            queryset = queryset.filter(province__icontains=province)
        if region_1 is not None:
            queryset = queryset.filter(region_1__icontains=region_1)
        if region_2 is not None:
            queryset = queryset.filter(region_1__icontains=region_2)
        if sort_order == 'ASC':
            queryset = queryset.order_by('price')
        if sort_order == 'DESC':
            queryset = queryset.order_by('price').reverse()
        return queryset

def loadData(path):
    df = pd.read_csv(path).replace(np.nan, None, regex=True)
    for index, row in df.iterrows():
        '''for j, column in row.iteritems():
            print(row[column],end='  ')
            if column=="points":
                row[column]=0
            elif column == "price":
                row[column] = 0.0

            else:
                row[column] = ''
        print()'''
        w = Wine(
            country = row['country'],
            description = row['description'],
            designation = row['designation'],
            points = row['points'],
            price = row['price'],
            province = row['province'],
            region_1 = row['region_1'],
            region_2 = row['region_2'],
            variety = row['variety'],
            winery = row['winery']
        )
        w.save()
        # print(row['c1'], row['c2'])


def LoadData(request):
    loadData('/home/ckrokad/Desktop/winedata.csv')
    return HttpResponse("data loaded")
