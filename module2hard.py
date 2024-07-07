def get_password(n):
    password = ""
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password

for i in range(3, 21):
    print(f"{i} - {get_password(i)}")