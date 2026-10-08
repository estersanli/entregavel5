import csv
import re


class FormatoInvalidoError(Exception):
    pass


def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao, email) is not None


def validar_cpf(cpf):
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return re.match(padrao, cpf) is not None


def validar_telefone(telefone):
    padrao = r"^\(\d{2}\) \d{5}-\d{4}$"
    return re.match(padrao, telefone) is not None


def validar_data(data):
    padrao = r"^\d{2}/\d{2}/\d{4}$"

    if not re.match(padrao, data):
        return False

    dia, mes, ano = data.split("/")

    if int(dia) < 1 or int(dia) > 31:
        return False

    if int(mes) < 1 or int(mes) > 12:
        return False

    return True


total = 0
validos = 0
invalidos = 0

registros_validos = []
registros_invalidos = []

arquivo = None

try:
    arquivo = open("dados.csv", "r", encoding="utf-8")

    leitor = csv.DictReader(arquivo)

    colunas = ["email", "cpf", "telefone", "data"]

    for coluna in colunas:
        if coluna not in leitor.fieldnames:
            raise KeyError(f"Coluna {coluna} não encontrada.")

    for linha in leitor:
        total += 1

        try:
            email = linha["email"]
            cpf = linha["cpf"]
            telefone = linha["telefone"]
            data = linha["data"]

            if not validar_email(email):
                raise FormatoInvalidoError("E-mail inválido.")

            if not validar_cpf(cpf):
                raise FormatoInvalidoError("CPF inválido.")

            if not validar_telefone(telefone):
                raise FormatoInvalidoError("Telefone inválido.")

            if not validar_data(data):
                raise FormatoInvalidoError("Data inválida.")

            registros_validos.append(linha)
            validos += 1

        except FormatoInvalidoError as erro:
            registros_invalidos.append((linha, str(erro)))
            invalidos += 1

except FileNotFoundError:
    print("Erro: arquivo dados.csv não encontrado.")

except KeyError as erro:
    print(f"Erro: coluna não encontrada - {erro}")

except ValueError:
    print("Erro: valor inválido.")

else:
    print("Arquivo lido com sucesso.")

finally:
    if arquivo is not None:
        arquivo.close()
    print("Leitura do arquivo finalizada.")


print("\n==============================")
print("RELATÓRIO FINAL")
print("==============================")

print(f"Total de registros: {total}")
print(f"Registros válidos: {validos}")
print(f"Registros inválidos: {invalidos}")

print("\nREGISTROS VÁLIDOS:")

for registro in registros_validos:
    print(
        f"E-mail: {registro['email']} | "
        f"CPF: {registro['cpf']} | "
        f"Telefone: {registro['telefone']} | "
        f"Data: {registro['data']}"
    )

print("\nREGISTROS INVÁLIDOS:")

for registro, erro in registros_invalidos:
    print(
        f"E-mail: {registro['email']} | "
        f"CPF: {registro['cpf']} | "
        f"Telefone: {registro['telefone']} | "
        f"Data: {registro['data']} | "
        f"Erro: {erro}"
    )