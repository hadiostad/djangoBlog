from django import forms
from .models import Comment


# A form for users to submit comments on a post.
class CommentForm(forms.ModelForm):
    class Meta:
        # Meta options for the CommentForm.
        model = Comment
        exclude = ["post"]
        labels = {
          "user_name": "Your Name",
          "user_email": "Your Email",
          "text": "Your Comment"
        }
