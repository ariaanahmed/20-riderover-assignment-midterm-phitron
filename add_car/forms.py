from django import forms
from .models import Car, Comment


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "car_title": forms.TextInput(attrs={"placeholder": "Title"}),
            "car_description": forms.Textarea(
                attrs={
                    "placeholder": "Description",
                    "style": "resize: none;",
                    "rows": 3,
                }
            ),
            "car_price": forms.TextInput(attrs={"placeholder": "Price"}),
            "brands": forms.Select(),
            "quantity": forms.NumberInput(attrs={"placeholder": "Quantity"}),
        }
        labels = {
            "car_img": "",
            "car_title": "",
            "car_description": "",
            "car_price": "",
            "brands": "",
            "quantity": "",
        }

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        self.fields["brands"].initial = 1

    def save(self, *args, **kwargs):
        print(self.cleaned_data["car_img"])
        return super().save(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "body": forms.Textarea(attrs={"placeholder": "Comment", "style": "resize: none;", "rows": 3}),
        }
        
        labels = {
            "name": "",
            "email": "",
            "body": "",
        }
