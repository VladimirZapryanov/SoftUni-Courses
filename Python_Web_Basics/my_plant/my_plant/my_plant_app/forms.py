from django import forms

from my_plant.my_plant_app.models import Profile, Plant


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreatePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'




