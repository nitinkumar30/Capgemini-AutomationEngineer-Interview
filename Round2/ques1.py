intro = {'name': 'Nitin', 'phone': 9137887, 'City': 'Pune'}
# out = {'name': 'nitiN', 'phone': 7887319, 'City': 'enuP'}

def reverse_string(s):
    result = ''
    i = len(s) - 1
    while i >= 0:
        result += s[i]
        i -= 1
    return result

out = {
    'name': reverse_string(intro['name']),
    'phone': int(reverse_string(str(intro['phone']))),
    'City': reverse_string(intro['City']),
}

print(out)
