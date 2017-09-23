from django import forms 
from devdebate.models import Opinion


class OpinionForm(forms.ModelForm):
	class Meta:
		model 	= Opinion
		fields 	= {'title', 'description', 'fororagainst'}
		widgets = {
            'title'  : forms.Textarea(
                attrs={
                'id'            : 'heading',
                'class'         : 'form-control bordr ',
                'placeholder'   : 'Heading..keep it short(within 100 words).',
                'rows'          : '2',
                'onkeyup'       : 'checklenchar()'
                }),
            'description'  : forms.Textarea(
                attrs={
                'id'            : 'desc',
                'class'         : 'form-control bordr ',
                'placeholder'   : 'Description..(within 1000 words).',
                'rows'          : '9',
                'onkeyup'       : 'checklenchar()'
                }),
            'fororagainst'  : forms.CheckboxInput(
                attrs={
                'id'            : 'myonoffswitch',
                'onclick'       : 'enabledisable()'
                }),          


            }