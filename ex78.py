import zlib
x ='HelloHelloHelloHello'
y = zlib.compress(x.encode("utf-8"))
print(y)
z = zlib.compress(x.encode("utf-16"))
print(z)
