def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def decrypt(private_key, encrypted):
    d, n = private_key
    decrypted = [(ord(char) ** d) % n for char in encrypted]
    output = [chr(char) for char in decrypted]
    return ''.join(output)


def encrypt(public_key, origin):
    e, n = public_key
    encrypted = [(ord(char) ** e) % n for char in origin]
    output = [chr(char) for char in encrypted]
    return ''.join(output)


def getPrivateKey(e, tot):
    d = 1
    while (e * d) % tot != 1 or d == e:
        d += 1
    return d


def getPublicKey(tot):
    e = 2
    while e < tot and gcd(e, tot) != 1:
        e += 1
    return e
