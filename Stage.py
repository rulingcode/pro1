def reverse(text: str) -> str:
    dv = ''
    for i in text:
        dv = i + dv
    return dv


text = "ew era gninrael .nohtyp"
list = text.split(' ')
text1 = ""
for i in list:
    end = (i == list[-1])
    i = reverse(i)
    if end:
        text1 = text1 + i
    else:
        text1 = text1 + i + ' '
print(text1)
