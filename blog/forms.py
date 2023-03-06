from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        labels = {
            'user_name ': 'Your Name',
            'email': 'Your Email',
            'comment_text': 'Your Comment'
        }