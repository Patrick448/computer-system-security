import math

from feistel import encrypt_decrypt_text, xor

IV = 0xa4439ccd729248b5     # hexadecimal aleatório
key = 0xd08044e0d9bf7565    # hexadecimal aleatório


def run_cbc(text_bytes):
    num_blocks = int(math.ceil(len(text_bytes)/8))
    result = []

    next_xor_input = IV.to_bytes(8, "big")
    for i in range(num_blocks):
        input_block = text_bytes[i*8:(i+1)*8]                                                 # seleciona próximo bloco de 8 bytes (64 bits)
        xor_output = xor(next_xor_input, input_block)                                         # xor
        cypher_output = encrypt_decrypt_text(xor_output, key.to_bytes(8, "big"), False)  # encripta resultado do xor
        result.append(cypher_output)                                                     # adiciona ao resultado final
        next_xor_input = cypher_output                                                   # próxima entrada do xor será o resultado desta iteração
        #print(text_bytes[i*8:(i+1)*8])

    #print(b''.join(result))
    return b''.join(result)


def run_cbc_decrypt(encrypted_input):
    num_blocks = int(math.ceil(len(encrypted_input)/8))
    result = []

    next_xor_input = IV.to_bytes(8, "big")
    for i in range(num_blocks):
        input_block = encrypted_input[i*8:(i+1)*8]
        cypher_output = encrypt_decrypt_text(input_block, key.to_bytes(8, "big"), True)
        xor_output = xor(next_xor_input, cypher_output)
        result.append(xor_output)
        next_xor_input = input_block
        #print(text_bytes[i*8:(i+1)*8])

    #print(b''.join(result).decode("UTF-8"))
    return b''.join(result).decode("UTF-8")


input_text = "segurança em sistemas de computação"
text_bytes = input_text.encode("UTF-8")
encypted = run_cbc(text_bytes)
print(f"Chave: {hex(key)}\nIV: {hex(IV)}\nEncriptado:\n{encypted}\n")
decrypted = run_cbc_decrypt(encypted)
print(f"Decriptado: {decrypted}")
