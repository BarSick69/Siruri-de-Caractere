S=input(str("dati sirul"))
print(S)
print("A,apare: ",S.count("A"))
print("Inlocuim A cu *: ",S.replace("A","*"))
A=[]
for i in range(0,len(S)):
    A.append(S[i])
A1=A.copy()
while "B" in A1:
    A1.remove("B")
L=""
L=L.join(A1)
print("Lista fara B: ",L)
print("MA apare: ",S.count("MA"))
print("Inlocuirea MA cu TA: ",S.replace("MA","TA"))
S1=S.replace("TO","")
txt=S1.strip()
print("S fara TO: ",txt)
A.reverse()
L=""
print(L.join(A))



    



