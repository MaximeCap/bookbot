def count_word(text):
    count = 0
    for word in text.split():
        count += 1
    return count


def count_char(text: str):
    dic: dict[str, int] = {}
    for cg in text.lower().replace(".", "").split(" "):
        for c in cg:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
    return dic


def get_char_dics(dic: dict[str, int]) -> []:
    char_dics = []
    for i in dic:
        if i.isalpha():
            char_dics.append({
                "char": i,
                "num": dic[i]
            })

    return char_dics
