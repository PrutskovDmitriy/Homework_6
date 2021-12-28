new_file = []
my_dict = dict()
with open('nginx_logs.txt', 'r', encoding='utf-8') as text:
    for my_file in text:
        my_text = my_file.split()
        numb = my_text[0]
        new_file.append((numb, my_text[5].strip('"'), my_text[6]))
        if numb not in my_dict:
            my_dict[numb] = 1
        else:
            my_dict[numb] += 1

m = 0
k = ''
for key, value in my_dict.items():
    if value > m:
        m = value
        k = key
print('Ip:', k, 'повторился:', m)
