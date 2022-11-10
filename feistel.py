# -*- coding: utf-8 -*-
# Aluno: Patrick Canto de Carvalho
# Matrícula: 201935026

# Implementação da cifra de feistel

import math


def to_byte_array(text):
    text_bytes = text.encode("UTF-8")
    padding = '#'.encode("UTF-8")
    return text_bytes.ljust(8, padding)


def rotate(byte_array):
    new_byte_array = byte_array[4:] + byte_array[:4]
    return new_byte_array


def f(bytes, key):
    result = int.from_bytes(bytes, 'big') & int.from_bytes(key, 'big')
    result = 1
    for byte in bytes:
        result *= byte
    #print(f"bytes: {bytes} : {len(bytes)} : {result}")
    return result.to_bytes(4, 'big')


def xor(byte_array1, byte_array2):
    result = int.from_bytes(byte_array1, 'big') ^ int.from_bytes(byte_array2, "big")
    return result.to_bytes(len(byte_array1), 'big')


def run_round(byte_array, key):
    left = byte_array[:4]
    right = byte_array[4:]

    result = right + xor(left, f(right, key))
    return result


def run_feistel(input_text_bytes, keys_list, rounds):
    result_block = input_text_bytes
    for i in range(rounds):
        result_block = run_round(result_block, keys_list[i])

    return result_block[4:] + result_block[:4]


def derive_keys(number, key):
    keys = []

    for i in range(number):
        new_key = (int.from_bytes(key[:4], 'big') + 2 ** i).to_bytes(4, 'big')
        keys.append(new_key)

    return keys


def encrypt_block(input_text_bytes, keys_list, rounds):
    result = run_feistel(input_text_bytes, keys_list, rounds)
    return result


def decrypt_block(hashed_text, keys_list, rounds):
    reversed_keys = keys_list
    reversed_keys.reverse()
    return run_feistel(hashed_text, reversed_keys, rounds)


def encrypt_decrypt_text(text_bytes, key, decrypt):
    input_len = len(text_bytes)
    blocks_list = []
    padding = '\0'.encode("UTF-8")
    keys_list = derive_keys(16, key)
    if decrypt:
        keys_list.reverse()

    for i in range(0, input_len, 8):
        block = ""
        if i+8 >= input_len:
            block = text_bytes[i:].ljust(8, padding)
        else:
            block = text_bytes[i:i+8]
        blocks_list.append(encrypt_block(block, keys_list, 16))

    return b''.join(blocks_list).strip(b'\0')


def main():
    input_text = input("Digite texto a ser criptografado: ")
    key = b'aacdefgh'

    encrypted_bytes = encrypt_decrypt_text(input_text.encode('UTF-8'), key, False)
    print("Texto criptografado (byte literal): " + str(encrypted_bytes))

    decrypted_bytes = encrypt_decrypt_text(encrypted_bytes, key, True)
    print("Texto descriptografado: " + decrypted_bytes.decode("UTF-8"))


if __name__ == "__main__":
    main()
