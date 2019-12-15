from django import forms

class CandidatesForm(forms.Form):
    fullname = forms.CharField(max_length=64)
    email = forms.EmailField()
    phone = forms.CharField(max_length=64)
    interested = forms.CharField(widget=forms.Textarea)
    github = forms.CharField(widget=forms.Textarea)
    article = forms.CharField(widget=forms.Textarea)
