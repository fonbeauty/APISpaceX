eng_chars = {1: 'AEIOULNSTR',
             2: 'DG',
             3: 'BCMP',
             4: 'FHVWY',
             5: 'K',
             9: 'JX',
             10: 'QZ'}


text = 'python'.upper()

result = 0
for char in text:
    for key, value in eng_chars.items():
        if char in value:
            result = result + key

key_result = [key for char in text for key, value in eng_chars.items() if char in value]

print(sum([key for char in text for key, value in eng_chars.items() if char in value]))

# print(result)


# А
# русские
# буквы
# оцениваются
# так:
# АВЕИНОРСТ–1
# очко;
# ДКЛМПУ–2
#
# БГЁЬЯ–3
#
# ЙЫ–4
#
# ЖЗХЦЧ–5
# очков;
# ШЭЮ–8
# очков;
# ФЩЪ–10
# очков.
