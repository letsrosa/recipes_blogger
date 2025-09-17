from django.db import models

class Receita(models.Model):
    CATEGORIAS = [
        ('comida', 'Comida'),
        ('drink', 'drink'),
        ('sobremesa', 'Sobremesa'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField (upload_to='receitas/images/',
    blank=True, null=True)
    
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS,
        default='comida')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ['-created_at'] 