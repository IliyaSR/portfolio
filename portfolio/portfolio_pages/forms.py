from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, label='',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'type': 'name'}), required=True)
    mail = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email'}))
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Text'}), required=True)
