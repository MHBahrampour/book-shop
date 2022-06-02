import imp
from django import forms

from .models import Contact


class CommentForm(forms.Form):

  SCORE_CHOICES = [
    ('', "Nothing Selected"),
    ('1', "1"),
    ('2', "2"),
    ('3', "3"),
    ('4', "4"),
    ('5', "5"),
  ]

  RECOMMEND_CHOICES = [
    ('', "Nothing Selected"),
    ('I Dont Recommend It', "I Dont Recommend It"),
    ('Not Sure To Recommend', "Not Sure To Recommend"),
    ('I Recommend It', "I Recommend It"),
  ]

  score = forms.ChoiceField(label='Score', choices=SCORE_CHOICES)

  recommend = forms.ChoiceField(label='Do you recommend this book?', choices=RECOMMEND_CHOICES)

  text = forms.CharField(label='Comment text', max_length=1000, widget=forms.Textarea)


class ContactForm(forms.ModelForm):

  class Meta:
    model   = Contact
    fields  = ('fullname', 'email', 'phone_number', 'subject', 'message')