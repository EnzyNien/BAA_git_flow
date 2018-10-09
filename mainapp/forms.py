
import django.forms as forms
from mainapp.models import Clients

def add_form_control_class(fields):
    for _, field in fields.items():
        field.widget.attrs['class'] = "form-control"

class ClientsEditForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('name', 'company', 'phone', 'email', 'interests')

    def __init__(self, *args, **kwargs):
        super(ClientsEditForm, self).__init__(*args, **kwargs)
        add_form_control_class(self.fields)

class ClientsAddForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('name', 'company', 'phone', 'email', 'interests')

    def __init__(self, *args, **kwargs):
        super(ClientsAddForm, self).__init__(*args, **kwargs)
        add_form_control_class(self.fields)

