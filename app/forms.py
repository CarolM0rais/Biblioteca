class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '_all_'

    def _init_(self, *args, **kwargs):
        super(LivroForm, self)._init_(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'titulo',
            'autor',
            'editora',
            'genero',
            'preco',
            'data_pub',
            'status',
            Submit('submit', 'Salvar')
        )