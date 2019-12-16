from django import forms

class CandidatesForm(forms.Form):
    fullname = forms.CharField(
        label = "Full Name",
        max_length = 64,
        required = True,
        )
    email = forms.EmailField()
    phone = forms.CharField(max_length=64)
    interested = forms.CharField(
        widget=forms.Textarea,
        label = "What are you interested in? What is your background?",
        required = True,
        )
    github = forms.CharField(
        widget=forms.Textarea,
        label = "Do you have a GitHub/Bitbucket account or links to sample code of yours that you can share?",
        required = True,
        )
    article = forms.CharField(
        widget=forms.Textarea,
        label = "What is the latest article that you read and influenced your work as an engineer and why?",
        required = True,
        )
