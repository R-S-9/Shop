from django import forms
from django.contrib import admin
from .models import *


class SweatshirtsCategoryChoiceField(forms.ModelChoiceField):
	pass


# Класс не позволяющий выбирать в категории другие товары.
class SweatshirtsAdmin(admin.ModelAdmin):

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'Category':
			return SweatshirtsCategoryChoiceField(Category.objects.filter(slug='Sweatshirtss'))
		return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Sweatshirts)
admin.site.register(Pants)
