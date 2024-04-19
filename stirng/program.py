#3
# st = 'w3'
# l=len(st)
# print(st[0:2]+st[(l-2):l])


#5
# s1 = input("s1")
# s2 = input("s2")
# l1=len(s1)
# l2=len(s2)

# print(s2[:2]+s1[2:]+' '+ s1[:2]+s2[2:])

#7 
st = 'The lyrics is not that poor!'
lt = st.split()
print(lt)
for i in range(len(lt)):
    if lt[i].lower() == "not":
        print(lt[i])
        for j in range(i,len(lt)):
            if lt[j].lower() == 'poor':
                lt[i,j+1]='good'
                break
print("".join(lt))