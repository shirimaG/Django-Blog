# CREATE A FORM SHARE EMAIL

from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)

#Form for users to comment on blog Post
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

#FORM TO ENABLE USERS TO ACCESS SEARCH FUNCTION

class SearchForm(forms.Form):
    query = forms.CharField()
    
