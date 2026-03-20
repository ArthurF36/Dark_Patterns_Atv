import json

def ler_arquivo_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Erro: Falha na sintaxe JSON do arquivo {nome_arquivo}.")
        return []