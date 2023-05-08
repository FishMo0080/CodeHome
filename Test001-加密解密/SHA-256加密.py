import hashlib
# 明文信息
plaintext = "mowenyu"
# 创建SHA-256对象
sha256 = hashlib.sha256()
# 将明文信息更新到SHA-256对象中
sha256.update(plaintext.encode('utf-8'))
# 获取SHA-256加密后的结果
ciphertext = sha256.hexdigest()
# 输出密文信息
print(ciphertext)