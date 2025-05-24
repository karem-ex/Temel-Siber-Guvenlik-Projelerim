import re as r
from time import time

common_passwords = ["123456",
                    "123456789",
                    "picture1",
                    "password",
                    "12345678",
                    "111111",
                    "123123",
                    "12345",
                    "1234567890",
                    "senha",
                    "1234567",
                    "qwerty",
                    "abc123",
                    "Million2",
                    "000000",
                    "1234",
                    "iloveyou",
                    "aaron431",
                    "password1",
                    "qqww1122"]
flag = True


def check_password_strength(password_: str):
    score = 0
    strength = ''

    # Parolanın havuzda kontrolü
    if password_.lower() in common_passwords:
        print("Parola çok yaygın! Lütfen daha güçlü bir şifre kullanın.")
        return "Zayıf", password_

    # Parolanın uzunluğunu denetleme
    if len(password_) < 8:
        print("Parola  8 karakter'den kısa...")
        score -= 1
    elif 8 <= len(password_) <= 12:
        print("Parola uzunluğu fena değil...")
        score += 1
    else:
        print("Parola çok güçlü...")
        score += 2

    # Parola karakter türleri kontrolü
    if r.search(r'[A-Z]', password_):
        score += 1
    else:
        print("Parola büyük harf içermiyor.")
        score -= 1

    if r.search(r'[a-z]', password_):
        score += 1
    else:
        print("Parola küçük harf içermiyor.")
        score -= 1

    if r.search(r'[0-9]', password_):
        score += 1
    else:
        print("Parola rakam içerimiyor.")
        score -= 1

    if r.search(r'\W', password_):
        score += 1
    else:
        print("Parola sembol içermiyor.")
        score -= 1

    # Parolayı puanlama

    if score <= 2:
        strength = "Zayıf"
    elif score <= 4:
        strength = "Orta"
    else:
        strength = "Güçlü"

    return f"Parola güvenirliği: {strength}\nParola: {password_}"
