from django.db import models







class Pharmacy(models.Model):
    title_medicine = models.CharField(max_length=100, verbose_name='Название лекарства')
    manufacturer = models.CharField(max_length=200, verbose_name='Производитель')
    descriptions = models.TextField('Описание', blank=True)
    price = models.IntegerField('Цена',)
    expiration_data = models.DateField('Дата окончания срока годности')
    count = models.IntegerField('Количество', default='0', blank=True)
    category = models.ForeignKey('medicine_category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категория лекарства')
    barcode = models.ImageField(upload_to='media/medicines_barcode/', verbose_name='Штрихкод товара', blank=True,
                                width_field='141px', height_field='98px')
    medicine_img = models.ImageField(upload_to='media/medicine_img/', verbose_name='Изображения лекарства', blank=True)
    code = models.CharField(max_length=48, verbose_name='Штрих-код(цифры)', blank=True)


    def __str__(self):
        return self.title_medicine

    class Meta:
        verbose_name = 'Лекарства'
        verbose_name_plural = 'Лекарства'


class Medicine_Category(models.Model):
    category = models.CharField(max_length=140, verbose_name='Категория')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория лекарства'
        verbose_name_plural = 'Категория лекарств'


class Medicine_Form(models.Model):
    form = models.CharField(max_length=140, verbose_name='Лекарственная форма')

    def __str__(self):
        return self.form

    class Meta:
        verbose_name = 'Лекарственная форма'
        verbose_name_plural = 'Лекарственая форма'



