import flet as ft
from Visualizacao.interface import Interface
from Dados.bancodeDados import BancoDeDados

def main(page: ft.Page):
    db = BancoDeDados("clinica_veterinaria.db")  # Cria a instância do banco de dados
    Interface(page, db)  # Passa a instância do banco de dados para a Interface
    
ft.app(target=main)
