# from .models import Module
# from django.forms import forms

# class ModuleForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ModuleForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'

#     class Meta:
#         model = Module
#         fields = ["title", "author", "body"]