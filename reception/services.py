from docxtpl import DocxTemplate

from reception.models import Receptions


def recieve_doc_create(Receptions, user):
    print(Receptions.objects.get(id=1))
    if Receptions.send_pdf_reciev_copy:
        doc = DocxTemplate("Vet_card_01.docx")
        context = { "Doctor": Receptions.doctor_set.doctor_name,
                    "first_name": Receptions.owner_name,
                    "last_name": Receptions.owner_lastname,
                    "father_name": Receptions.owner_lastname,
                    "tel": Receptions.owner_email,
                    "pet_kind": Receptions.kind_of_pet_rec,
                    "data": Receptions.data_receptions,

        }
        doc.render(context)
        doc.save(f'Прием от {Receptions.data_receptions}, {Receptions.owner_name} {Receptions.owner_lastname}.docx')