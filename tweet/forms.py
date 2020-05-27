from django import forms
from tweet.models import Tweet


class AddTweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['tweet']
