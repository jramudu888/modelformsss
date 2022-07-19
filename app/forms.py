from django import forms

from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fileds='__all__'
        fields=['topic_name','url']
        exclude=['topic_name','url']
        widgets={'name':forms.PasswordInput}
        widgets={'name':forms.Textarea()}