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
	shipping = models.ForeignKey(
		verbose_name='배송정책',
		to='goods.Shipping',
		related_name='goods',
		on_delete=models.PROTECT,
		null=False,
	)

	def __str__(self):
		return self.name


class Option(models.Model):
	"""
	StyleShare Goods 의 Options
	"""
	goods = models.ForeignKey(
		verbose_name='어떤 Goods 의 Option 인지',
		to='goods.Goods',
		related_name='option',
		on_delete=models.CASCADE,
		null=True
	)
	color = models.CharField(
		verbose_name='옵션 색상',
		max_length=55,
		choices=[
			('yellow', '노랑'), ('blue', '파랑'), ('red', '빨강'), ('green', '초록'), ('yellowgreen', '연초록'),
			('violet', '자주'), ('black', '검정'),
		],
		null=False,
		blank=True,
		default="yellow",
	)
	size = models.CharField(
		verbose_name='옵션 색상',
		max_length=55,
		choices=[
			('S', 'small'), ('M', 'medium'), ('L', 'large'), ('XL', 'extra large'),
		],
		null=False,
		blank=True,
		default="S",
	)
	stock = models.PositiveIntegerField(
		verbose_name='옵션 재고 수량',
		null=False,
		default=0,
	)

	def save(self, *args, **kwargs):

		# Data Integrity
		# 중복된 정보는 저장 불가능하다
		if Option.objects.filter(goods=self.goods, color=self.color, size=self.size).count() > 0:
			return

		# 저장한다.
		super().save(*args, **kwargs)

	def __str__(self):
		if not self.goods:
			return "No Goods Assigned"
		else:
			return "[" + self.goods.name + "]" + self.color + "|" + self.size


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

	def __str__(self):
		return self.name


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

		# Data Integrity
		# 중복된 정보는 저장 불가능하다
		if Shipping.objects.filter(method=self.method, price=self.price, can_bundle=self.can_bundle).count() > 0:
			return

		# 저장한다.
		super().save(*args, **kwargs)

	def __str__(self):
		can_bundle_kr = '묶음 가능' if self.can_bundle else '묶음 불가'
		return self.method + '|' + str(self.price ) + '|' + can_bundle_kr
