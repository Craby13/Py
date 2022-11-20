print("Bonjour, que voulez-vous faire ?")
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for x in range(len(list)):
    list.append(list[x])
    
msg = input("Veuillez indiqué le message crypté: ")
key = int(input("Veuillez indiqué la clé de chiffrement"))

def décryptage_msg(lettre, liste, clef):
    for i in range(len(list)):
        if lettre == ' ':
            return ' '
        elif list[i]==lettre:
            return str(list[i-key])
    return '?'

message_décrypté = str()

for lettre in msg:
    message_décrypté += décryptage_msg(lettre, list, key)

print(message_décrypté)



