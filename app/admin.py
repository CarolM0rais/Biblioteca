from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Livro, Genero, Reserva


class ReservaInline(admin.TabularInline):
    model = Reserva
    extra = 1

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1


class LivroEditoraInline(admin.TabularInline):
    model = Livro
    extra = 1


class ReservaLeitorInline(admin.TabularInline):
    model = Reserva
    extra = 1

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'editora', 'genero', 'preco', 'data_pub', 'status')
    inlines = [ReservaInline]


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    inlines = [LivroInline]


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site', 'cidade')
    inlines = [LivroEditoraInline]


@admin.register(Leitor)
class LeitorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cpf')
    inlines = [ReservaLeitorInline]


admin.site.register(Cidade)
admin.site.register(Genero)
admin.site.register(Reserva)  
