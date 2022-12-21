def greeting(jam = 6):
    if jam < 12:
        return "Selamat Pagi!"
    elif jam < 18:
        return "Selamat Sore!"
    else:
        return "Selamat Malam!"

print(greeting(6))