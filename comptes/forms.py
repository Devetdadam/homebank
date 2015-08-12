from django.forms import ModelForm
# from django.contrib.auth.models import User
from .models import Compte


class CompteForm(ModelForm):
    class Meta:
        model = Compte
        fields = ['compte', 'alias']


# class MetacategorieForm(ModelForm):
#     class Meta:
#         model = Categorie
#         fields = ['categorie']
