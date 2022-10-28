#Program To Convert Integers Into Roman Numbers

charset = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),
           (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),
           (9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
def to_roman(n):
    rn = ''
    while n > 0:
        for k , m in charset:
            while n >= k:
                rn += m
                n -= k
        return rn

num = int(input("Enter An Integer :- "))
print("Roman Value Of",num,"is",to_roman(num))
