from django import forms

from .models import Driver


class DriverForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Driver
        fields = '__all__'

        def __init__(self, *arg, **kwargs):
            super(DriverForm, self).__init__(*arg, **kwargs)
            for field_name, field in self.fileds.items():
                field.widget.attrs['class'] = 'form-control'
