from django.forms import ModelForm, Textarea
from models import CustomerReviews

class CustomerReviewForm(ModelForm):

    class Meta:
        model= CustomerReviews
        fields = ('review_title','review')
        widgets = {
            'review': Textarea,
        }
