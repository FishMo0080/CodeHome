import hashlib
# 明文信息
plaintext = "Lis225588"
# 创建SHA-512对象
sha512 = hashlib.sha512()
# 将明文信息更新到SHA-512对象中
sha512.update(plaintext.encode('utf-8'))
# 获取SHA-512加密后的结果
ciphertext = sha512.hexdigest()
# 输出密文信息
print(ciphertext)