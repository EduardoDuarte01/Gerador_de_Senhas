#Progeto para gerar senhas automáticas para os usuários. Espero que gostem!
import secrets
from string import ascii_letters, digits

symbols = '!#$%&()*+><^~@-_çÇ`/|ªº¿'
alphabet = ascii_letters + digits + symbols

# eu não colocaria quantidades específicas de cada tipo (X letras, Y números, etc)
# talvez a quantidade mínima para alguns (abaixo vejo se tem pelo menos 3 dígitos)
# em vez disso, verifico se tem pelo menos um de cada
tamanho_senha = 16
while True:
    password = ''.join(secrets.choice(alphabet) for _ in range(tamanho_senha))
    if (any(c.islower() for c in password) # tem alguma letra minúscula
            and any(c.isupper() for c in password) # tem alguma letra maiúscula
            and any(c in symbols for c in password) # tem algum símbolo
            and sum(c.isdigit() for c in password) >= 3): # tem pelo menos 3 dígitos
        break # deu certo, sai do while

print(password)