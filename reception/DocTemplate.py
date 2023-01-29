
# from docxtpl import DocxTemplate
# from docx2pdf import convert
# from pathlib import Path
# from reception.views import reception_request
#
#
# def RecievDocs(context):
#     RecievDoc = DocxTemplate('reception/doc-pdf-fuller/Vet_card_01.docx')
#     context = {
#         'Doctor': form.cleaned_data["time_to_come"]
#     }
#     RecievDoc.render(context)
#     RecievDoc.save(f'reception/doc-pdf-fuller/Vet_card_DATA_{context["Doctor"]}.docx')
#     # Open Docx to convert to pdf
#     DocToConvert = Document(f'reception/doc-pdf-fuller/Vet_card_DATA_{context["Doctor"]}.docx')
#     # Convert to pdf
#     DocToConvert.save(f'reception/doc-pdf-fuller/Vet_card_DATA_{context["Doctor"]}.pdf')
