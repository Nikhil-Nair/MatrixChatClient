from django import forms


class MessageInputForm(forms.Form):
    messageText = forms.CharField(label='Message', max_length=150)
