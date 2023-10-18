import hashlib


def get_hash_password(user, p):
    st= user+p
    h1=hashlib.sha1(st.encode("utf-8"))
    return str(h1.hexdigest())
