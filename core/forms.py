from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField

class BenForm(forms.Form):
    form_method = 'get'
    ben = forms.CharField(
        label = "Billed Entity Number (BEN)",
        help_text = "Enter the full BEN here",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'ben',
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
