# Outer Import
from django.db import models


# Create your models here.

class Goods(models.Model):
	"""
	StyleShare Store 의 상품
	"""
	name = models.CharField(
		verbose_name="상품명",
		max_length=255,
		null=False,
		blank=True,
		default="",
	)
	provider = models.ForeignKey(
		verbose_name='제공자',
		to='goods.Provider',
		related_name='goods',
		on_delete=models.CASCADE,
		null=True
	)
	price = models.PositiveIntegerField(
		verbose_name='가격',
		null=False,
		default=0,
	)
	shipping = models.OneToOneField(
		verbose_name='배송정책',
		to='goods.Shipping',
		related_name='goods',
		on_delete=models.PROTECT,
		null=False,
	)


class Option(models.Model):
	"""
	StyleShare Goods 의 Options
	"""
	goods = models.ForeignKey(
		verbose_name='어떤 Goods 의 Option 인지',
		to='goods.Goods',
		related_name='options',
		on_delete=models.CASCADE,
		null=True
	)
	color = models.CharField(
		verbose_name='옵션 색상',
		max_length=55,
		null=False,
		blank=True,
		default="",
	)
	size = models.CharField(
		verbose_name='옵션 색상',
		max_length=55,
		null=False,
		blank=True,
		default="",
	)
	stock = models.PositiveIntegerField(
		verbose_name='옵션 재고 수량',
		null=False,
		default=0,
	)


class Provider(models.Model):
	"""
	StyleShare 의 상품 공급자
	"""
	name = models.CharField(
		verbose_name="공급자명",
		max_length=255,
		null=False,
		blank=True,
		default="",
	)


class Shipping(models.Model):
	"""
	Goods 배송정책
	"""
	method = models.CharField(
		verbose_name='배송비 부과 여부',
		max_length=10,
		choices=[('FREE', '무료 배송'), ('PREPAY', '유료 배송')],
		null=False,
		default='FREE',
	)
	price = models.PositiveIntegerField(
		verbose_name='가격',
		null=False,
		default=0,
	)
	can_bundle = models.BooleanField(
		verbose_name='묶음 배송 가능 여부',
		null=False,
		default=True,
	)

	def save(self, *args, **kwargs):
		# Data Integrity
		# method FREE 일 때 price 무조건 0 으로 set 한다.
		if self.method == "FREE":
			self.price = 0

		# 저장한다.
		super().save(*args, **kwargs)
