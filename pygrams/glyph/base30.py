

def conv24300000(n):
    q = n // 24300000
    r = n % 24300000
    x = list(conv810000(r))
    y = [q] + x
    return y

def conv810000(n):
    q = n // 810000
    r = n % 810000
    x = list(conv27000(r))
    y = [q] + x
    return y

def conv27000(n):
    q = n // 27000
    r = n % 27000
    x = list(conv900(r))
    y = [q] + x
    return y

def conv900(n):
    q = n // 900
    r = n % 900
    x = list(conv30(r))
    y = [q] + x
    return y

def conv30(n):
    q = n // 30
    r = n % 30
    x = [q,r]
    return  x


def converter(n):
    n = int(n)
    if n <= 30:
        c = conv30(n)
    elif 30 < n <= 900:
        c = conv900(n)
    elif 900 < n <= 27000:
        c = conv27000(n)
    elif 27000 < n <= 810000:
        c = conv810000(n)
    elif 810000 < n <= 24300000:
        c = conv24300000(n)
    
    while c[0] == 0:
        c.pop(0)
    return c


#print(converter(12345678)) #debug
