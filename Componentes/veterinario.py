from Visualizacao.usuario import Usuario

class Veterinario(Usuario):
    def __init__(self, nome, telefone, especialidade):
        super().__init__(nome, telefone)
        self._especialidade = especialidade

    def salvar(self, banco_de_dados):
        banco_de_dados.adicionar_veterinario(self._nome, self._telefone, self._especialidade)
        
    @staticmethod
    def consultar(banco_de_dados, nome=None, id_veterinario=None):
        if nome:
           resultado = banco_de_dados.consultar_veterinario(nome=nome)
        elif id_veterinario:
            resultado = banco_de_dados.consultar_veterinario(id_veterinario=id_veterinario)
        else:
            return None

        if resultado:
            # Transforme a tupla em um dicionário
            return {
                'id': resultado[0],
                'nome': resultado[1],
                'telefone': resultado[2],
                'especialidade': resultado[3]
            }
        return None

    def atualizar(self, banco_de_dados, id_veterinario, nome=None, telefone=None, especialidade=None):
        banco_de_dados.atualizar_veterinario(id_veterinario, nome or self._nome, telefone or self._telefone, especialidade or self._especialidade)

    @staticmethod
    def remover(banco_de_dados, id_veterinario):
        banco_de_dados.remover_veterinario(id_veterinario)


