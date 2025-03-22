from django import forms

class CadastroForm(forms.Form):
    nom = forms.CharField(max_length=100, label="Nom")
    prenom = forms.CharField(max_length=100, label="Prénom")
    date_naissance = forms.DateField(label="Date de naissance", widget=forms.DateInput(attrs={'type': 'date'}))
    passport = forms.CharField(max_length=50, label="Passport")
    rnm = forms.CharField(max_length=50, label="RNM")
    adresse = forms.CharField(widget=forms.Textarea, label="Adresse complète")
    ville = forms.CharField(max_length=100, label="Ville")
    etat = forms.CharField(max_length=100, label="État")
    contact = forms.CharField(max_length=20, label="Contact")
    email = forms.EmailField(label="E-mail")
    etudiant = forms.ChoiceField(
        label="Vous êtes étudiant ?",
        choices=[('sim', 'Oui'), ('nao', 'Non')],
        widget=forms.Select(attrs={'onchange': 'toggleCampos()'})
    )
    cours = forms.CharField(max_length=200, required=False, label="Cours")
    etablissement = forms.CharField(max_length=200, required=False, label="Établissement")
    profession = forms.CharField(max_length=200, required=False, label="Profession")