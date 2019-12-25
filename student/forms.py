from django import forms
from .models import Student

# class StudentForm(forms.Form):
#     name=forms.CharField(max_length=128,label='姓名')
#     sex=forms.ChoiceField(choices=Student.SEX_ITEMS,label='性别')
#     profession=forms.CharField(max_length=128,label='职业')
#     email=forms.EmailField(max_length=128,label='Email')
#     qq=forms.CharField(max_length=128,label='QQ')
#     phone=forms.CharField(max_length=128,label='电话')

class StudentForm(forms.ModelForm):

    def clean_qq(self):
        cleaned_data=self.cleaned_data['qq']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('QQ必须是数字')
        return int(cleaned_data)

    class Meta:
        model=Student
        fields=('name','sex','profession','email','qq','phone')



