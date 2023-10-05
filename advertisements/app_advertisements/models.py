from django.db import models

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=35)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_length=10, decimal_places=2, max_digits=20)
    auction = models.BooleanField("торг", help_text="Ответьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.price}, price={self.price: .2f})>'
