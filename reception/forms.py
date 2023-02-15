import datetime

from django import forms
from django.forms import DateInput

from .models import RecieveRequsetModel, Receptions




def now_data():
    now = datetime.datetime.now()
    today_date = now.strftime("%Y-%m-%d")
    return today_date


# def date_validator():



def time_unique():

    """ Вырезает время, на которое уже была запись из общего словаря """

    work_time = {
            ("9:00", "9:00"), ("16:00", "16:00"),
            ("9:30", "9:30"), ("16:30", "16:30"),
            ("10:00", "10:00"), ("17:00", "17:00"),
            ("10:30", "10:30"), ("17:30", "17:30"),
            ("11:00", "11:00"), ("18:00", "18:00"),
            ("11:30", "11:30"), ("18:30", "18:30"),
            ("12:00", "12:00"), ("19:00", "19:00"),
            ("12:30", "12:30"), ("19:30", "19:30"),
            ("13:00", "13:00"), ("20:00", "20:00"),
            ("13:30", "13:30"), ("20:30", "20:30"),
            ("14:00", "14:00"), ("21:00", "21:00"),
            ("14:30", "14:30"), ("21:30", "21:30"),
            ("15:00", "15:00"), ("22:00", "22:00"),
            ("15:30", "15:30"),
    }

    WORK_TIME = work_time
    for i in list(WORK_TIME):
        if RecieveRequsetModel.objects.filter(time_to_come=i[0]).count() == 0:
            continue
        else:
            WORK_TIME.discard(i)
    return WORK_TIME



WORK_TIME = time_unique()


class RecievRequestForm(forms.ModelForm):
    time_to_come = forms.ChoiceField(choices=WORK_TIME)

    class Meta:

        model = RecieveRequsetModel
        fields = ('derscription', 'data_to_come', 'time_to_come', 'email_recive', 'tel_num',
                  'pet_name', 'pet_owner', 'status', 'id',)
        widgets = {
             'data_to_come': DateInput(
                 attrs={'type': 'date', "min": now_data}
             )
            # 'time_to_come': SelectDateWidget(
            #     attrs={'type':'time', 'min':'09:00', 'max':'22:00', 'step':'1800'}
            # )
         }


class RecieveForm(forms.ModelForm):


    class Meta:

        model = Receptions
        fields = ('owner_name', 'kind_of_pet_rec', 'pet_gender_rec', 'pet_nickname_rec', 'doctor',
                  'rec_diagnose', 'rec_instructions', 'owner_email', "rec_medicine", 'send_pdf_reciev_copy', 'owner_tel')










