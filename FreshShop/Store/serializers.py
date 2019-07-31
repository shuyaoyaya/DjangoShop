from rest_framework import serializers

from Store.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Goods
        fields = ['goods_name','goods_price','goods_number','goods_description']


class GoodsTypeSerializer(serializers.HyperlinkedModelSerializer):
    """
    声明查询的表和返回的字段
    """
    class Meta:
        model = GoodsType
        fields = ["name","description"]

