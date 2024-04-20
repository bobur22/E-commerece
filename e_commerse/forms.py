from django import forms
from .models import shopModel

class uploadFile(forms.ModelForm):
    # file = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True}))
    class Meta:
        model = shopModel
        fields = ['name', 'price', 'detail', 'images', "p_size"]
        widgets = {
            'images': forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": True})),
            # 'region': forms.Select(attrs={'class': 'form-control'}),
            # 'address': forms.Textarea(attrs={
            #     'class': 'form-control pt-2 pt-sm-3',
            #     'style': 'resize: none; margin-top: 5px; height: min(12vw, 65px);',
            # }),
            # 'news_agreement': forms.CheckboxInput(attrs={
            #     'class': 'reg-checkbox news-agree-check position-absolute z-2',
            #     'onclick': "regCheckboxValidate()"
            # }),
            # 'profile_img': forms.FileInput(attrs={
            #     'class': 'form-control pt-2 pt-sm-3',
            #     'accept': ".jpg, .jpeg, .png"})
        }