# 두 수 a, b의 최대공약수를 구하는 함수
def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


# Public key 'e'를 구하는 함수
def getPublicKey(tot):
    e = 2
    while e < tot and gcd(e, tot) != 1:
        e += 1
    return e


# Private key 'd'를 구하는 함수
def getPrivateKey(e, tot):
    d = 1
    while (e * d) % tot != 1 or d == e:
        d += 1
    return d


# 암호화 함수
def encrypt(public_key, origin):
    e, n = public_key
    encrypted = [(ord(char) ** e) % n for char in origin]
    output = [chr(char) for char in encrypted]
    return ''.join(output)


# 복호화 함수
def decrypt(private_key, encrypted_text):
    d, n = private_key
    decrypted = [(ord(char) ** d) % n for char in encrypted_text]
    output = [chr(char) for char in decrypted]
    return ''.join(output)
