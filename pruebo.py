def ultima_aparicion2(s: list[int], e: int) -> int:
    aparicion: int = 0

    for i in range(len(s)):
        if s[i] == e:
            aparicion = i
    return aparicion

print(ultima_aparicion2([-1,4,0,4,100,0,100,0,-1,-1], 0))
print(ultima_aparicion2([1,2,120,1,567,0,9,0,1,5,6], 1))