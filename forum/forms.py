from django import forms


class MessageForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'input_form', 'placeholder': 'Leave your message here'}))
    reply_id = forms.IntegerField(label='', required=False, widget=forms.Textarea(attrs={
        'hidden': 'true', 'id': 'reply_id_field'}))


class PostForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'title_form', 'placeholder': 'Post title'}))
    text = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'input_form', 'placeholder': 'Enter your post here'}))
