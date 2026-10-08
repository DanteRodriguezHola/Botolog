from django.forms import ModelForm

from .models import Comment

class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['user'].widget.attrs.update({'class': 'form short'})
        self.fields['content'].widget.attrs.update({'class': 'form long'})

    class Meta:
        model = Comment
        fields = ('user', 'content')