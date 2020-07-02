from django import forms
from ghostpost.models import Post


class add_post_forms(forms.Form):

    post_type = forms.BooleanField(label="Boast or Roast?",required=False)
    message = forms.CharField(label='Post', max_length=280, required=True, widget=forms.Textarea)

