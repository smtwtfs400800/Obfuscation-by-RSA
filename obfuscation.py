import rsa
from pathlib import Path

FILE = Path(__file__).resolve()
print(FILE)
ROOT = FILE.parent

if __name__ == '__main__':
    # 키 생성
    p, q = 991, 997
    n = p * q
    tot = (p - 1) * (q - 1)
    e = rsa.getPublicKey(tot)
    d = rsa.getPrivateKey(e, tot)

    origin = open(ROOT / 'test.py', 'r+', encoding='utf-8')
    encrypted = open(ROOT / 'encrypted.py', 'a+', encoding='utf-8')
    decrypted = open(ROOT / 'decrypted.py', 'a+', encoding='utf-8')

    origin_text = origin.readlines()
    encrypted_text = []
    decrypted_text = []

    for line in origin_text:
        is_encrypt = line.find('encrypt')
        is_def = line.find('def')

        if is_encrypt >= 0 and is_def == -1:
            line = line.replace('encrypt', 'decrypt')
            start = line.find('(')
            end = line.find(')')
            str = line[start + 2: end - 1]
            line = line.replace(str, rsa.encrypt((e, n), str))

        encrypted_text.append(line)

    encrypted.write(''.join(encrypted_text))

    for line in encrypted_text:
        is_decrypt = line.find('decrypt')
        is_def = line.find('def')

        if is_decrypt >= 0 and is_def == -1:
            line = line.replace('decrypt', 'encrypt')
            start = line.find('(')
            end = line.find(')')
            str = line[start + 2: end - 1]
            line = line.replace(str, rsa.decrypt((d, n), str))

        decrypted_text.append(line)

    decrypted.write(''.join(decrypted_text))
