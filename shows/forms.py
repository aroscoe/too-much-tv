from django import forms

from shows.models import Show

class ShowForm(forms.ModelForm):
    
    class Meta:
        model = Show
        exclude = ('slug',)

class ShowSearchForm(forms.Form):
    show = forms.CharField()
    
    def clean_show(self):
        show = self.cleaned_data['show']
        if Show.objects.filter(name__iexact=show):
            raise forms.ValidationError("You have already added this show!")
        return show