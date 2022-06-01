from django import forms

class CommentForm(forms.Form):

  SCORE_CHOICES = [
    ('1', "1"),
    ('2', "2"),
    ('3', "3"),
    ('4', "4"),
    ('5', "5"),
  ]

  RECOMMEND_CHOICES = [
    ('I Dont Recommend It', "I Dont Recommend It"),
    ('Not Sure To Recommend', "Not Sure To Recommend"),
    ('I Recommend It', "I Recommend It"),
  ]

  score = forms.ChoiceField(label='Score', choices=SCORE_CHOICES, widget=forms.RadioSelect)

  recommend = forms.ChoiceField(label='Do you recommend this book?', choices=RECOMMEND_CHOICES, widget=forms.RadioSelect)

  text = forms.CharField(label='Comment text', max_length=1000, widget=forms.Textarea)

  