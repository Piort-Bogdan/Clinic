
from docxtpl import DocxTemplate
from docx2pdf import convert
from pathlib import Path


RecievDoc = DocxTemplate('Vet_card_01.docx')
context = {
    'Doctor': "Саведий"
}
RecievDoc.render(context)
RecievDoc.save('Vet_card_DATA_NAME.docx')

convert('Vet_card_DATA_NAME.docx')
