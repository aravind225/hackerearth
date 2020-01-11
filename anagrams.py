def makeAnagram(a, b): 
    buffer = [0] * 26
    for char in a: 
        buffer[ord(char) - ord('a')] += 1
    for char in b: 
        buffer[ord(char) - ord('a')] -= 1
    print(buffer)
    print(sum(map(abs,buffer)))
    return sum(map(abs, buffer))
t=int(input())
l=[]
for _ in range(t):
    str1 = input()
    str2 = input()
    l.append(makeAnagram(str1, str2)) 
for i in l:
    print(i)
