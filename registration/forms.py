from django.contrib.auth import authenticate
from django import forms



class AuthenticationForm(forms.Form):
    username = forms.CharField(label="Username",max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError(f'there is not {username} in my users')


# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(max_length=254, help_text=u'Обязательно укажите действующий адрес эл. почты.', label=u'Эл. почта')
#
#     class Meta:
#         model = MyUser
#         fields = ('username', 'email', 'password1', 'password2', )
