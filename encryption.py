import string

def encrypt(message, key):
    char = string.ascii_letters + string.punctuation
    delim = ''
    for l in message:
        if l in char:
            lno = char.find(l)
            delim_no = (lno + key) % len(char)
            delim += char[delim_no]
        else:
            delim += l
    return delim
