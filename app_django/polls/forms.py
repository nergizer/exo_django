from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(label="Question", max_length=100,required=True)
    reponse0 = forms.CharField(label="Réponse", max_length=100,required=True)
    reponse1 = forms.CharField(label="Réponse", max_length=100,required=False)
    reponse2 = forms.CharField(label="Réponse", max_length=100,required=False)