import bcrypt

# Contraseña a cifrar
password = "mi_contraseña_secreta".encode("utf-8")

# Generar un salt
salt = bcrypt.gensalt()

# Cifrar la contraseña
hashed = bcrypt.hashpw(password, salt)

print("Contraseña original:", password)
print("Hash generado:", hashed)

# Verificar la contraseña
if bcrypt.checkpw(password, hashed):
    print("¡La contraseña es correcta!")
else:
    print("La contraseña es incorrecta.")