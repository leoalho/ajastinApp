import bcrypt

def time_to_string(time):
    """Luo merkkijonoesityksen

    Args:
        time (int): aika

    Returns:
        Palauttaa merkkijonona ajan
    """
    if not time:
        return "0 s"
    remaining = time
    result = ""
    if remaining>3600:
        hours = remaining//3600
        remaining -= hours*3600
        result += f"{hours} h "
        if remaining<60:
            result += "0 m "
    if remaining>60:
        minutes = remaining//60
        remaining -= minutes*60
        result += f"{minutes} m "
    result += f"{remaining} s"
    return result

def hash_password(password):
    """Luo hashatun salasanan

    Args:
        password (string): Salasana, joka halutaan hashata

    Returns:
        Palauttaa hashatun salasanan merkkijonona
    """

    encoded_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    decoded_hash = hashed_password.decode('utf-8')
    return decoded_hash

def validate_password(password, user):
    """Validoi salasanan

    Args:
        password: salasana
        user: Käyttäjä

    Returns:
       Palauttaa True, jos salasanat täsmäävät, muutoin False
    """
    encoded_password = password.encode('utf8')
    return bcrypt.checkpw(encoded_password, user[2].encode('utf8'))
