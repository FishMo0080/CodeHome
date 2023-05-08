def caesar_cipher_encrypt(plaintext, shift):  
    ciphertext = ""  
    for char in plaintext:  
        if char.isalpha(): # 仅对字母进行加密  
            ascii_code = ord(char) + shift  
            if char.isupper():  
                if ascii_code > ord('Z'):  
                    ascii_code -= 26  
                elif ascii_code < ord('A'):  
                    ascii_code += 26  
            elif char.islower():  
                if ascii_code > ord('z'):  
                    ascii_code -= 26  
                elif ascii_code < ord('a'):  
                    ascii_code += 26  
            ciphertext += chr(ascii_code)  
        else:  
            ciphertext += char  
    return ciphertext  
  
def caesar_cipher_decrypt(ciphertext, shift):  
    return caesar_cipher_encrypt(ciphertext, -shift) # 反向凯撒密码加密  
  
# 示例用法  
plaintext = "Hello, World!"  
shift = 3  
ciphertext = caesar_cipher_encrypt(plaintext, shift)  
print("加密后的密文：", ciphertext)  
decrypted_text = caesar_cipher_decrypt(ciphertext, shift)  
print("解密后的明文：", decrypted_text)