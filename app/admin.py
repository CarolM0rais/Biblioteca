from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Livro, Genero

# Inline de Livro no admin do Autor
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1  # Número de livros adicionais visíveis por padrão

# Configuração personalizada para o admin de Autor
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [LivroInline]  # Exibe livros diretamente no admin de Autor

# Registro dos modelos no admin
admin.site.register(Cidade)
admin.site.register(Autor, AutorAdmin)  # Usa a versão personalizada com inline
admin.site.register(Editora)
admin.site.register(Leitor)
admin.site.register(Livro)
admin.site.register(Genero)
