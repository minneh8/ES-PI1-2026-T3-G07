"""
Módulo de Condições Globais.

Armazena variáveis globais utilizadas pelo sistema eleitoral,
permitindo o compartilhamento de estados, menus, conexões com
o banco de dados e informações temporárias entre os módulos.
"""

menu_principal = -1  
menu_gerenciamento = -1  
menu_votacao = -1  
menu_candidatos = -1
menu_eleitores = -1
menu_sistem_votacao = -1
menu_auditoria = -1
menu_resultado = -1
menu_edicaodados = -1
menu_buscacandidatos = -1
menu_listacandidatos = -1
menu_removecandidatos = -1
menu_cadastramento_cand = -1
menu_listaeleitores = -1
menu_removeeleitores = -1   
menu_buscaeleitores = -1
menu_edicaodados_ele = -1
menu_cadastramento_ele = -1
menu_para_votacao = -1
tela_login = -1
estado = " "
nome = " "
sobrenome = " "
cpf = 0
teleitor = 0
cursor = 0
cadastro = 0
senha = " "
valores = 0
connection = 0
cpfvalido = True
teleitorvalido = 0
sistema_votacao_aberto = False
protocolo = 0
mesario = 0
cpf_eleitor = 0
eleitor = 0
confirmar_voto = "N"