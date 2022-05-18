import csv
import io
from django import forms


class StudForm(forms.Form):
    ID =	forms.IntegerField()
    first_name	=	forms.CharField(max_length=50)
    last_name	=	forms.CharField(max_length=50)
    email	=	forms.EmailField(max_length=50)
    gender	=	forms.CharField(max_length=50)
    school	=	forms.CharField(max_length=50)
    books=	forms.CharField(max_length=50)

class Ssearch(forms.Form):
    first_name = forms.CharField(max_length=50,required=False)
    ID = forms.IntegerField(required=False)

# class CSVupload(forms.Form):
#     data_file = forms.FileField()
    
#     def process_file(self):
#         f = io.TextIOWrapper(self.cleaned_data['data_file'].file)
#         reader = csv.DictReader(f)

#         for row in reader:

