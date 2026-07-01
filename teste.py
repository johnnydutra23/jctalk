def conta_somatoria(valores):
    """Retorna a soma dos valores passados em uma lista ou iterável."""
    return sum(valores)

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    resultado = conta_somatoria(numeros)
    print("Hoje e dia dos namorados com a Luana")
    print(f"Somatória de {numeros} = {resultado}")
