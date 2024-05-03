n = int(input(""))
lts=list(map(int,input().split(" ")))



d=dict()
m=0
for i in lts:
    d[i] = d.get(i,0)+1
    if m<d[i]:
        m=d[i]

c=0
for i in d.values():
    if m==i:
        c+=1
print(c)

# def character_frequency(string):
#     # Initialize an empty dictionary to store the character frequencies
#     freq = {}
    
#     # Iterate through each character in the string
#     for char in string:
#         # Increment the count of the character in the dictionary
#         freq[char] = freq.get(char, 0) + 1
    
#     return freq

# # Sample String
# sample_string = "google.com"

# # Get the character frequency
# result = character_frequency(sample_string)

# # Print the result
# print("Expected Result:", result)
