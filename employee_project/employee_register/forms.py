from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullname','mobile' ,'emp' ,'position')
        labels = {
            'fullname' : 'Full Name',
            'emp':'EMP Code'
        }

    def __init__(self,*args , **kwargs):
        super(EmployeeForm,self).__init__(*args , **kwargs)
        self.fields['position'].empty_label ='Select'
        self.fields['emp'].required =False