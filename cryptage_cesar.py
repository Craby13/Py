list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for x in range(len(list)):
    list.append(list[x])

msg = input("Veuillez votre message: ")
key = int(input("Veuillez indiqué la clé de chiffrement: "))

def cryptage_msg(lettre, liste, key):
    for i in range(len(list)):
        if lettre == ' ':
            return ' '
        elif list[i]==lettre:
               return str(list[i+key])
    return '?'
message_crypté = str()

for lettre in msg:
    message_crypté += cryptage_msg(lettre, list, key)

print(message_crypté)