# Exercicio 1 - Aquecendo os motores

usuarios = [
    {'nome': 'Bianca', 'idade': '23', 'cidade': 'Manaus', 'estado': 'Amazonas'},
    {'nome': 'Luís', 'idade': '47', 'cidade': 'Portão', 'estado': 'Rio Grande do Sul'},
    {'nome': 'Tatiane', 'idade': '45', 'cidade': '', 'estado': 'Ceará'},
    {'nome': '', 'idade': '27', 'cidade': 'Manuas', 'estado': 'Amazonas'},
    {'nome': 'Alexandre', 'idade': '29', 'cidade': 'Manuas', 'estado': 'Amazonas'}
]


# Exercicio 2 - Perfil
def criando_pefil(usuarios):
    perfis = []
    perfil = {
        'nome': str,
        'idade': int,
        'localizacao': (str, str),
    }

    for usuario in usuarios:
        perfil['nome'] = usuario['nome']
        perfil['idade'] = usuario['idade']
        perfil['localizacao'] = (usuario['cidade'], usuario['estado'])

        perfis.append(perfil)

    print(perfis)


# Exercicio 3 - Comparando Estruturas

'''
    Lista = para coleções mutáveis de dados
        - Mutável - pode ser modificada (adicionar, remover ou alterar)
        - Indexada - os elementos são acessados por índices numérios
        - Uso - ideal para armazenar uma coleção de elementos ordenados, como uma lista de IDs de usuários
        
    id_usuarios = [101, 102, 103, 104] (Lista de id de usuarios)
    
    Dicionário = para associas pares de dados
        - Mutável - pode ser modificado, mas com pares de chave-valor
        - Não ordenado - os elementos são acessados por chaves (que pordem ser strings, números, etc...)
        - Uso - ideal para armazenar dados em pares de chave-valor, como o nome do usuario associado ao seu id
        
    data_usuarios = {101: 'Alice', 102: 'Bob'} (id de usuario e nome)
    
    Tupla = para dados imutáveis
        Imutável - não pode ser alterada após a criação
        Indexada - os elementos são acessados por índices numérios
        Uso - ideal para armazenar dados que não devem ser alterados como um par de coordenadas geográficas de um local
        
    localizacao = (40.2781, -37.2642) (Coordenadas geograficas de um local)
'''


# Exercicio 4 - Limpando o terreno

def validar_perfil(perfis):
    perfis_validados = []
    for perfil in perfis:
        if perfil['nome'] is not None or perfil['cidade'] is not None:
            perfis_validados.append(perfil)

    print(perfis_validados)

# Exercicio 5 - Carregando dados

# Exercicio 6 - Concatenando dados

# Exercicio 7 - Adicionando Amigos

# Exercicio 8 - Verificando Conexões

# Exercicio 9 - Amigos em Comum

# Exercicio 10 - Conexões Exclusivas

# Exercicio 11 - Removendo Conexões

# Exercicio 12 - Salvando o Progresso

# Exercicio 13 - Listando Usuários

# Exercicio 14 - Quantidade de Amigos

# Exercicio 15 - Usuários Mais Populares

# Exercicio 16 - Lidando com arquivos
