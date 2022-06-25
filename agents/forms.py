from django import forms
from django.contrib.auth import get_user_model


class AgentModelForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
        )
