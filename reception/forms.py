import datetime

from django import forms
from django.forms import DateInput, TimeInput, ChoiceField, SelectDateWidget

from .models import RecieveRequsetModel

def now_data():
    now = datetime.datetime.now()
    today_date = now.strftime("%Y-%m-%d")
    return today_date


class RecievRequestForm(forms.ModelForm):
    WORK_TIME = {
        ("9:00","9:00"),      ("16:00","16:00"),
        ("9:30","9:30"),      ("16:30","16:30"),
        ("10:00","10:00"),    ("17:00","17:00"),
        ("10:30","10:30"),    ("17:30","17:30"),
        ("11:00","11:00"),    ("18:00","18:00"),
        ("11:30","11:30"),    ("18:30","18:30"),
        ("12:00","12:00"),    ("19:00","19:00"),
        ("12:30","12:30"),    ("19:30","19:30"),
        ("13:00","13:00"),    ("20:00","20:00"),
        ("13:30","13:30"),    ("20:30","20:30"),
        ("14:00","14:00"),    ("21:00","21:00"),
        ("14:30","14:30"),    ("21:30","21:30"),
        ("15:00","15:00"),    ("22:00","22:00"),
        ("15:30","15:30"),
    }
    time_to_come = forms.ChoiceField(choices=WORK_TIME)

    class Meta:

        model = RecieveRequsetModel
        fields = ('derscription', 'data_to_come', 'time_to_come', 'email_recive', 'tel_num',
                  'pet_name', 'pet_owner', 'status',)
        widgets = {
             'data_to_come': DateInput(
                 attrs={'type': 'date', "min": now_data}
             )
            # 'time_to_come': SelectDateWidget(
            #     attrs={'type':'time', 'min':'09:00', 'max':'22:00', 'step':'1800'}
            # )
         }


class CategoryChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "tel: {}".format(obj.owner_tel)










