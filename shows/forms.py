from django import forms

from shows.models import Show

class ShowForm(forms.ModelForm):
    # TODO: add validation to check and see if that show is already in the db
    
    class Meta:
        model = Show

class ShowSearchForm(forms.Form):
    show = forms.CharField()
    
    def clean_show(self):
        show = self.cleaned_data['show']
        if Show.objects.filter(name__iexact=show):
            raise forms.ValidationError("You have already added this show!")
        return show