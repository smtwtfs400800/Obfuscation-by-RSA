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
    public_key = (e, n)

    origin_file = open(ROOT/'test.py', 'r+', encoding='utf-8')
    encrypted_file = open(ROOT/'encryption_result.py', 'a+', encoding='utf-8')

    origin_text = origin_file.readlines()
    encrypted_text = []
    decrypted_text = []

    # 암호화 과정
    for line in origin_text:
        is_encrypt = line.find('encrypt')
        is_def = line.find('def')
        is_comment = line.find('#')

        # 주석 암호화
        if is_comment >= 0:
            str = line[is_comment + 1: -1]
            line = line.replace(str, rsa.encrypt(public_key, str))

        # 암호화하려는 문자열 암호화
        elif is_def == -1 and is_encrypt >= 0:
            line = line.replace('encrypt', 'decrypt')
            start = line.find('(')
            end = line.find(')')
            str = line[start + 2: end - 1]
            line = line.replace(str, rsa.encrypt(public_key, str))

        encrypted_text.append(line)

    encrypted_file.write(''.join(encrypted_text))
