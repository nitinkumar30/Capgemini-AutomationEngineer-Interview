D={1:"a",7:"b",3:"e",11:"z",21:"o"}
# print the sum of all the keys whose value is a vowel in the English alphabet.

rslt = sum(key for key, value in D.items() if value in {'a', 'e', 'i', 'o', 'u'})
print(rslt)

# Interviewer actually asked me to code 1 liner for this problem statement
