import math

def le_arquivo(nome_arquivo):
    '''Essa função lê o arquivo e retorna uma lista com o que tem no arquivo'''
    arquivo = open(nome_arquivo, "r")

    for linha in arquivo:
        caracteres = list(map(int, linha.split()))

    arquivo.close()
    return caracteres

def criptografa_tabela_ascii(n, e):
    '''Essa função criptografa todos os 128 caracteres ascii com a chave pública enviada por parâmetro.
    Retorna um dicionario sendo a chave o caracter criptografado e o valor sendo o valor da tabela ascii'''
    tabela_ascii_criptografada = {}

    for numero_ascii in range(0,128):
        numero_criptografado = pow(numero_ascii, e) % n
        tabela_ascii_criptografada[numero_criptografado] = numero_ascii

    return tabela_ascii_criptografada

def descriptografa_texto(caracteres, tabela_ascii_criptografada):
    '''Recebe uma lista com os caracteres que devem ser descriptografas e a tabela ascii criptografas.
    Retorna o texto descriptografado'''
    mensagem_descriptografada = ''

    for numero_criptografado in caracteres:
        if numero_criptografado in tabela_ascii_criptografada:
            mensagem_descriptografada = mensagem_descriptografada + str(chr(tabela_ascii_criptografada[numero_criptografado]))

    return mensagem_descriptografada

if __name__ == "__main__":
    n = 3424467341
    e = 17
    nome_arquivo = "mensagem_criptografada"

    caracteres = le_arquivo(nome_arquivo)
    tabela_ascii_criptografada = criptografa_tabela_ascii(n, e)
    texto_descriptografada = descriptografa_texto(caracteres, tabela_ascii_criptografada)
    
    print(texto_descriptografada)