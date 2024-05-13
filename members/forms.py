from django.forms import ModelForm
from django import forms
from .models import Member


class ProjectForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TimeInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            # 'gender':forms.TextInput(attrs={'class':'form-control'}),
            'joined_date':forms.DateInput(attrs={'class':'form-control'}),
            # 'image':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),



    

        }