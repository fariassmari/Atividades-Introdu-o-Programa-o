def media_aritmetica(n1:int, n2: int, n3:int) -> int:
    return (n1 + n2 + n3) /3

def media_ponderada(n1:int, n2:int, n3:int, p1:int, p2:int, p3:int) -> int:
    return (n1*p1 + n2*p2 + n3*p3) / (p1 + p2 + p3) 
