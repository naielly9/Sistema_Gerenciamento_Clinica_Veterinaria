import flet as ft
from Componentes.veterinario import Veterinario

class Interface:
    def __init__(self, page, db):
        self.page = page
        self.page.title = "Sistema de Gerenciamento de Clínica Veterinária"
        self._db = db  # Atributo privado
        self.mostrar_menu()

    def mostrar_menu(self):
        menu = ft.Column([
            ft.Text("Gerenciar Veterinários", size=20, weight="bold"),
            ft.ElevatedButton(text="Cadastrar Veterinário", on_click=lambda e: self.solicitarDados("cadastrar")),
            ft.ElevatedButton(text="Consultar Veterinário", on_click=lambda e: self.solicitarDados("consultar")),
            ft.ElevatedButton(text="Atualizar Veterinário", on_click=lambda e: self.solicitarDados("atualizar")),
            ft.ElevatedButton(text="Remover Veterinário", on_click=lambda e: self.solicitarDados("remover")),
            # Adicione outros botões para Tutores, Animais e Procedimentos
        ])

         # Caminhos das imagens
        image_paths = [f"Visualizacao/Imagem/Img{i}.jpeg" for i in range(1, 8)]

        # Carregar imagens
        imagens = []
        for path in image_paths:
            try:
                imagem = ft.Image(src=path, width=200, height=200)
                imagens.append(imagem)
            except Exception as e:
                print(f"Erro ao carregar a imagem: {path} - {e}")
                imagens.append(ft.Text(f"Erro ao carregar a imagem: {path}"))

        linhas = []
        for i in range(0, len(imagens), 3):
            linha = ft.Row(imagens[i:i + 3], alignment="center")
            linhas.append(linha)

        imagens_colunas = ft.Column(linhas, expand=True)

        conteudo = ft.Row([menu, imagens_colunas], expand=True)
        self.page.controls = [conteudo]
        self.page.update()  # Atualiza a página para exibir o menu

    def solicitarDados(self, acao):
        def on_submit(e):
            valores = [field.value for field in input_fields]
            if acao == "cadastrar":
                veterinario = Veterinario(valores[0], valores[1], valores[2])
                veterinario.salvar(self._db)
                self._exibir_dados(f"Veterinário {valores[0]} cadastrado com sucesso!")
            elif acao == "consultar":
                dados = Veterinario.consultar(self._db, nome=valores[0]) or Veterinario.consultar(self._db, id_veterinario=valores[0])
                if dados:
                    self._exibir_veterinario(dados)
                else:
                    self._exibir_dados("Veterinário não encontrado.")
                return  # Adiciona um retorno aqui para não limpar e mostrar o menu novamente
            elif acao == "atualizar":
                veterinario = Veterinario(valores[1], valores[2], valores[3])
                veterinario.atualizar(self._db, valores[0], valores[1], valores[2], valores[3])
                self._exibir_dados("Veterinário atualizado com sucesso!")
            elif acao == "remover":
                Veterinario.remover(self._db, valores[0])
                self._exibir_dados("Veterinário removido com sucesso!")
            self.page.controls = []  # Limpa a página após o envio
            self.mostrar_menu()  # Mostra o menu novamente

        # Cria campos e botão de envio baseados na ação
        if acao == "cadastrar":
            input_fields = [ft.TextField(label="Nome"), ft.TextField(label="Telefone"), ft.TextField(label="Especialidade")]
            submit_button = ft.ElevatedButton(text="Cadastrar", on_click=on_submit)
        elif acao == "consultar":
            input_fields = [ft.TextField(label="Nome ou ID do Veterinário")]
            submit_button = ft.ElevatedButton(text="Consultar", on_click=on_submit)
        elif acao == "atualizar":
            input_fields = [ft.TextField(label="ID do Veterinário"), ft.TextField(label="Nome (opcional)"), ft.TextField(label="Telefone (opcional)"), ft.TextField(label="Especialidade (opcional)")]
            submit_button = ft.ElevatedButton(text="Atualizar", on_click=on_submit)
        elif acao == "remover":
            input_fields = [ft.TextField(label="ID do Veterinário")]
            submit_button = ft.ElevatedButton(text="Remover", on_click=on_submit)

        self.page.controls = input_fields + [submit_button]
        self.page.update()  # Atualiza a página para exibir os novos controles

    def _exibir_dados(self, dados):
        self.page.controls = [ft.Text(dados), ft.ElevatedButton(text="Menu Principal", on_click=lambda e: self.mostrar_menu())]
        self.page.update()

    def _exibir_veterinario(self, dados):
        input_fields = [
            ft.TextField(label="Nome", value=dados['nome'], disabled=True),
            ft.TextField(label="Telefone", value=dados['telefone'], disabled=True),
            ft.TextField(label="Especialidade", value=dados['especialidade'], disabled=True)
        ]
        voltar_button = ft.ElevatedButton(text="Menu Principal", on_click=lambda e: self.mostrar_menu())
        self.page.controls = input_fields + [voltar_button]
        self.page.update()
