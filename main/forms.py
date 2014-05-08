from django.forms import ModelForm, Textarea
from models import CustomerReviews
from django import forms

class CustomerReviewForm(ModelForm):
    review_title = forms.CharField(required=True)
    review = forms.CharField(required=True, widget=Textarea)

    class Meta:
        model= CustomerReviews
        fields = ('review_title','review')
