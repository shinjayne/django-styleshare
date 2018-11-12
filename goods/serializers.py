# Outer Import
from rest_framework import serializers as serz

# Inner Import
from goods.models import Goods, Option, Provider, Shipping


class OptionSerializer(serz.ModelSerializer):
	class Meta:
		model = Option
		fields = (
			'id', 'color', 'size', 'stock'
		)


class ShippingSerializer(serz.ModelSerializer):

	canBundle = serz.BooleanField(
		help_text='묶음 배송 가능한지',
		source='can_bundle'
	)

	class Meta:
		model = Shipping
		fields = (
			'id', 'method', 'price', 'canBundle'
		)


class GoodsListSerializer(serz.ModelSerializer):
	provider = serz.CharField(
		help_text='제공자 이름',
		source='provider.name',
	)

	class Meta:
		model = Goods
		fields = (
			'id', 'name', 'price', 'provider',
		)


class GoodsSerializer(serz.ModelSerializer):
	provider = serz.CharField(
		help_text='제공자 이름',
		source='provider.name',
	)

	options = OptionSerializer(
		help_text='옵션들',
		many=True,
		source='option',
	)

	shipping = ShippingSerializer(
		help_text='배송정보',
	)

	class Meta:
		model = Goods
		fields = (
			'id', 'name', 'price', 'provider', 'options', 'shipping',
		)
