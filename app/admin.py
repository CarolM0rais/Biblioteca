from django.contrib import admin
from .models import Cidade, Autor, Editora, Leitor, Livro, Genero, Reserva


class ReservaInline(admin.TabularInline):
    model = Reserva
    extra = 1


class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1


class ReservaLeitorInline(admin.TabularInline):
    model = Reserva
    extra = 1


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'editora', 'genero', 'preco', 'data_pub', 'status')
    list_filter = ('status', 'genero', 'editora')
    search_fields = ('nome', 'autor__nome', 'editora__nome')
    inlines = [ReservaInline]


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade__nome')
    inlines = [LivroInline]


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site', 'cidade')
    search_fields = ('nome', 'cidade__nome')
    inlines = [LivroInline]


@admin.register(Leitor)
class LeitorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cpf')
    search_fields = ('nome', 'email', 'cpf')
    inlines = [ReservaLeitorInline]


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('livro', 'leitor', 'data_reserva', 'data_devolucao', 'devolvido')
    list_filter = ('devolvido', 'data_reserva')
    search_fields = ('livro__nome', 'leitor__nome')


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    search_fields = ('nome',)


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
