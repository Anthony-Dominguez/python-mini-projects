import bcrypt

salt = bcrypt.gensalt()

mypassword = b"anthony"

hashed = bcrypt.hashpw(mypassword, salt)



def check_password(hashed, user_password):
    if bcrypt.checkpw(user_password, hashed):
        return True
    else:
        return False  
      

print(check_password(hashed, mypassword))
print(check_password(hashed, b"wrongpassword"))