def xoa_ky_tu_lap(word):
    if not word:
        return word
    
    ket_qua = word[0]
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            ket_qua += word[i]
    return ket_qua

def remove_reduntdant_char(text):
    phu_am = ['ch', 'nh', 'th', 'kh', 'gi', 'ng', 'ph', 'gh', 'ngh']
    chars = []
    indexof_char = []

    for pa in phu_am:
        if text.startswith(pa):
            chars.append(pa)
            indexof_char.append(0)
            text = text[len(pa):]
            break

    return text, chars, indexof_char


def change_alias(alias):
    telex_map = {
        # a
        'af': 'à', 'as': 'á', 'aj': 'ạ', 'ar': 'ả', 'ax': 'ã',
        'aa': 'â', 'aaf': 'ầ', 'aas': 'ấ', 'aaj': 'ậ', 'aar': 'ẩ', 'aax': 'ẫ',
        'aw': 'ă', 'awf': 'ằ', 'aws': 'ắ', 'awj': 'ặ', 'awr': 'ẳ', 'awx': 'ẵ',
        # e
        'ee': 'ê', 'eef': 'ề', 'ees': 'ế', 'eej': 'ệ', 'eer': 'ể', 'eex': 'ễ',
        'ef': 'è', 'es': 'é', 'ej': 'ẹ', 'er': 'ẻ', 'ex': 'ẽ',
        # i
        'if': 'ì', 'is': 'í', 'ij': 'ị', 'ir': 'ỉ', 'ix': 'ĩ',
        # o
        'oo': 'ô', 'oof': 'ồ', 'oos': 'ố', 'ooj': 'ộ', 'oor': 'ổ', 'oox': 'ỗ',
        'ow': 'ơ', 'owf': 'ờ', 'ows': 'ớ', 'owj': 'ợ', 'owr': 'ở', 'owx': 'ỡ',
        'of': 'ò', 'os': 'ó', 'oj': 'ọ', 'or': 'ỏ', 'ox': 'õ',
        # u
        'uw': 'ư', 'uwf': 'ừ', 'uws': 'ứ', 'uwj': 'ự', 'uwr': 'ử', 'uwx': 'ữ',
        'uf': 'ù', 'us': 'ú', 'uj': 'ụ', 'ur': 'ủ', 'ux': 'ũ',
        # y
        'yf': 'ỳ', 'ys': 'ý', 'yj': 'ỵ', 'yr': 'ỷ', 'yx': 'ỹ',
        # d
        'dd': 'đ'
    }

    str_ = alias.lower()
    process, char_deleted, _ = remove_reduntdant_char(str_)

    # Ưu tiên chuỗi dài
    for length in range(4, 1, -1):
        for i in range(len(process) - length + 1):
            key = process[i:i + length]
            if key in telex_map:
                process = process[:i] + telex_map[key] + process[i + length:]
                return "".join(char_deleted) + process

    if process in telex_map:
        process = telex_map[process]

    return "".join(char_deleted) + process

def xu_ly_tu(word):
    word = xoa_ky_tu_lap(word)   # bước 1: dư chữ
    word = change_alias(word)   # bước 2: telex
    return word


def process_error_text(text):
    words = text.split()
    return " ".join(xu_ly_tu(w) for w in words)

if __name__ == "__main__":
    error_text = input("Nhập câu cần xử lý: ")
    print("Kết quả:", process_error_text(error_text))
