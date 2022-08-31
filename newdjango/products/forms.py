from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title','description','price'
		]
	def clean_title(self,*args,**kwargs): #overriden function; clean_title function is bydefault called by django
		title = self.cleaned_data.get("title")
		if not "CFE" in title:
			raise forms.ValidationError("This is not allowed")
		return title


class RawProductForm(forms.Form):
	title = forms.CharField(label = '')
	description = forms.CharField(required = False)
	price = forms.DecimalField(initial = 199)
			

