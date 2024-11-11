from django import forms
from .models import Profile, DynamicField

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'age']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in DynamicField.objects.all():
            if field.field_type == 'char':
                self.fields[field.name] = forms.CharField(
                    max_length=field.max_length,
                    required=False
                )
            elif field.field_type == 'int':
                self.fields[field.name] = forms.IntegerField(required=False)

    def save(self, commit=True):
        profile = super().save(commit=False)
        dynamic_data = {}
        for field in DynamicField.objects.all():
            dynamic_data[field.name] = self.cleaned_data.get(field.name)
        profile.additional_data = dynamic_data
        if commit:
            profile.save()
        return profile

class DynamicFieldForm(forms.ModelForm):
    class Meta:
        model = DynamicField
        fields = ['name', 'field_type', 'max_length']
