# Exercício sobre Cifra de César.
# Criar um código (em qualquer linguagem) que implemente a Cifra de Substituição de César.
# Depois mostre a frequência das letras na palavra Cifrada.

print("Aula 5 - criptografia")

text = input("Digite o texto a ser criptografado: ")
shift = input("Digite o deslocamento:")
result = ""


def encrypt(text, shift):
    result = ""
    for c in text:
        new_code = (ord(c) - 97) % 26
        result += chr(new_code + 97 + int(shift))

    return result


def decrypt(text, shift):
    result = ""
    for c in text:
        new_code = (ord(c) - 97 - int(shift)) % 26
        result += chr(new_code + 97)

    return result


def generate_freqs(text):
    freq_dict = {}
    total_chars = 0

    for c in text:
        if c not in freq_dict:
            freq_dict[c] = 1
        else:
            freq_dict[c] += 1
        total_chars+=1

    for key in freq_dict:
        freq_dict[key] = freq_dict[key]/total_chars

    return freq_dict


encrypted = encrypt(text, shift)
print("Texto criptografado:")
print(encrypted+"\n")
#print(decrypt(encrypted, shift))

print("Frequências relativas dos caracteres:")
print(generate_freqs(encrypted))

