from django import forms


class VotingForm(forms.Form):
    choices = forms.TypedChoiceField(
        choices=[],
        coerce=int,
        widget=forms.RadioSelect()
    )

    def __init__(self, *args, **kwargs):
        poll_choices = kwargs.pop('poll_choices', None)
        print(poll_choices)
        super(VotingForm, self).__init__(*args, **kwargs)
        self.fields['choices'].choices = poll_choices or []
