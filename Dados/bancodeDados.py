import sqlite3

class BancoDeDados:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        # Habilitar suporte a chaves estrangeiras
        self.cursor.execute('PRAGMA foreign_keys = ON;')
        self._criar_tabelas()

    def _criar_tabelas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS veterinario (
                id_veterinario INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                especialidade TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tutor (
                id_tutor INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                endereco TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS animal (
                id_animal INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                especie TEXT,
                raca TEXT,
                idade INTEGER NOT NULL,
                id_tutor INTEGER,
                FOREIGN KEY (id_tutor) REFERENCES tutor(id_tutor)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS procedimento (
                id_procedimento INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                descricao TEXT,
                data DATETIME,
                id_veterinario INTEGER,
                id_animal INTEGER,
                FOREIGN KEY (id_veterinario) REFERENCES veterinario(id_veterinario),
                FOREIGN KEY (id_animal) REFERENCES animal(id_animal)
            )
        ''')
        self.connection.commit()
        
    def adicionar_veterinario(self, nome, telefone, especialidade):
        self.cursor.execute(
            "INSERT INTO veterinario(nome, telefone, especialidade) VALUES (?, ?, ?)", 
            (nome, telefone, especialidade)
        )
        self.connection.commit()
        
    def consultar_veterinario(self, nome=None, id_veterinario=None):
        if nome:
            self.cursor.execute("SELECT * FROM veterinario WHERE nome = ?", (nome,))
        elif id_veterinario:
            self.cursor.execute("SELECT * FROM veterinario WHERE id_veterinario = ?", (id_veterinario,))
        else:
            raise ValueError("Deve fornecer nome ou id_veterinario")
        return self.cursor.fetchone()
    
    def atualizar_veterinario(self, id_veterinario, nome=None, telefone=None, especialidade=None):
        query = "UPDATE veterinario SET"
        params = []

        if nome is not None:
            query += " nome = ?,"
            params.append(nome)
        if telefone is not None:
            query += " telefone = ?,"
            params.append(telefone)
        if especialidade is not None:
            query += " especialidade = ?,"
            params.append(especialidade)

        query = query.rstrip(',') + " WHERE id_veterinario = ?"
        params.append(id_veterinario)

        self.cursor.execute(query, params)
        self.connection.commit()
        
    def remover_veterinario(self, id_veterinario):
        self.cursor.execute("DELETE FROM veterinario WHERE id_veterinario = ?", (id_veterinario,))
        self.connection.commit()

    def adicionar_tutor(self, nome, telefone, endereco):
        self.cursor.execute(
            "INSERT INTO tutor (nome, telefone, endereco) VALUES (?, ?, ?)", 
            (nome, telefone, endereco)
        )
        self.connection.commit()

    def consultar_tutor(self, nome=None, id_tutor=None):
        if nome:
            self.cursor.execute("SELECT * FROM tutor WHERE nome = ?", (nome,))
        elif id_tutor:
            self.cursor.execute("SELECT * FROM tutor WHERE id_tutor = ?", (id_tutor,))
        else:
            raise ValueError("Deve fornecer nome ou id_tutor")
        return self.cursor.fetchone()

    def atualizar_tutor(self, id_tutor, nome=None, telefone=None, endereco=None):
        query = "UPDATE tutor SET"
        params = []

        if nome is not None:
            query += " nome = ?,"
            params.append(nome)
        if telefone is not None:
            query += " telefone = ?,"
            params.append(telefone)
        if endereco is not None:
            query += " endereco = ?,"
            params.append(endereco)

        query = query.rstrip(',') + " WHERE id_tutor = ?"
        params.append(id_tutor)

        self.cursor.execute(query, params)
        self.connection.commit()
        
    def remover_tutor(self, id_tutor):
        self.cursor.execute("DELETE FROM tutor WHERE id_tutor = ?", (id_tutor,))
        self.connection.commit()

    def adicionar_animal(self, nome, especie, raca, idade, id_tutor):
        self.cursor.execute(
            "INSERT INTO animal (nome, especie, raca, idade, id_tutor) VALUES (?, ?, ?, ?, ?)", 
            (nome, especie, raca, idade, id_tutor)
        )
        self.connection.commit()

    def remover_animal(self, id_animal):
        self.cursor.execute("DELETE FROM animal WHERE id_animal = ?", (id_animal,))
        self.connection.commit()
        
    def consultar_animal(self, nome=None, id_animal=None):
        if nome:
            self.cursor.execute("SELECT * FROM animal WHERE nome = ?", (nome,))
        elif id_animal:
            self.cursor.execute("SELECT * FROM animal WHERE id_animal = ?", (id_animal,))
        else:
            raise ValueError("Deve fornecer nome ou id_animal")
        return self.cursor.fetchone()
    
    def atualizar_animal(self, id_animal, nome=None, especie=None, raca=None, idade=None, id_tutor=None):
        query = "UPDATE animal SET"
        params = []

        if nome is not None:
            query += " nome = ?,"
            params.append(nome)
        if especie is not None:
            query += " especie = ?,"
            params.append(especie)
        if raca is not None:
            query += " raca = ?,"
            params.append(raca)
        if idade is not None:
            query += " idade = ?,"
            params.append(idade)
        if id_tutor is not None:
            query += " id_tutor = ?,"
            params.append(id_tutor)

        query = query.rstrip(',') + " WHERE id_animal = ?"
        params.append(id_animal)

        self.cursor.execute(query, params)
        self.connection.commit()

    def adicionar_procedimento(self, tipo, descricao, data, id_veterinario, id_animal):
        self.cursor.execute(
            "INSERT INTO procedimento (tipo, descricao, data, id_veterinario, id_animal) VALUES (?, ?, ?, ?, ?)", 
            (tipo, descricao, data, id_veterinario, id_animal)
        )
        self.connection.commit()
        
    def consultar_procedimento(self, tipo=None, id_procedimento=None):
        if tipo:
            self.cursor.execute("SELECT * FROM procedimento WHERE tipo = ?", (tipo,))
        elif id_procedimento:
            self.cursor.execute("SELECT * FROM procedimento WHERE id_procedimento = ?", (id_procedimento,))
        else:
            raise ValueError("Deve fornecer tipo ou id_procedimento")
        return self.cursor.fetchone()
    
    def atualizar_procedimento(self, id_procedimento, tipo=None, descricao=None, data=None, id_veterinario=None, id_animal=None):
        query = "UPDATE procedimento SET"
        params = []

        if tipo is not None:
            query += " tipo = ?,"
            params.append(tipo)
        if descricao is not None:
            query += " descricao = ?,"
            params.append(descricao)
        if data is not None:
            query += " data = ?,"
            params.append(data)
        if id_veterinario is not None:
            query += " id_veterinario = ?,"
            params.append(id_veterinario)
        if id_animal is not None:
            query += " id_animal = ?,"
            params.append(id_animal)

        query = query.rstrip(',') + " WHERE id_procedimento = ?"
        params.append(id_procedimento)

        self.cursor.execute(query, params)
        self.connection.commit()
        
    def remover_procedimento(self, id_procedimento):
        self.cursor.execute("DELETE FROM procedimento WHERE id_procedimento = ?", (id_procedimento,))
        self.connection.commit()

    def close(self):
        self.connection.close()
