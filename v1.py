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


NGUYEN_AM = set("aeiouy")

VAN_HOP_LE = {
    "a","ai","ao","au","ay",
    "e","eo","em","en","et",
    "i","ia","iu",
    "o","oa","oe","oi",
    "u","ua","ui",
    "y","ya","ye"
}

def sua_du_nguyen_am_trong_van(process):
    # nếu vần đã hợp lệ thì giữ nguyên
    if process in VAN_HOP_LE:
        return process

    # thử xóa từng nguyên âm
    for i in range(len(process)):
        if process[i] in NGUYEN_AM:
            new_van = process[:i] + process[i+1:]
            if new_van in VAN_HOP_LE:
                return new_van

    return process


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
    process = sua_du_nguyen_am_trong_van(process)

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

def process_error_text(text):
    words = text.split()
    return " ".join(xu_ly_tu(w) for w in words)

def sua_loi_chinh_ta(word):
    word = word.lower()

    # dùng hàm tách phụ âm đầu của bạn
    van, chars, _ = remove_reduntdant_char(word)
    phu_am = "".join(chars)

    # Dictionary phụ âm đầu → vần hợp lệ
    PHU_AM_VAN = {
        "ngh": {"e","em","en","eng","ê","êm","ên","êng","i","in","inh"},
        "gh":  {"e","em","en","eng","ê","êm","ên","êng","i","in","inh"},
        "q":   {"u","ua","ui","um","un","ung"},
        "k":   {"e","em","en","eng","ê","êm","ên","êng","i","in","inh"},
        "c":   {"a","ai","ao","au","am","an","ang","ac","at","o","oi","om","on","ong","u","ung"},
        "g":   {"a","ai","ao","am","an","ang","o","oi","om","on","ong","u","ung"},
        "ph":  {"a","ai","ao","am","an","ang","u","ui","um","un","ung","o","on","ong","ơ"},
        "th":  {"a","ai","ao","am","an","ang","u","ui","ung","o","om","on","ong","i","ia"},
        "ng":  {"a","ai","am","an","ang","o","oi","om","on","ong","u","ung","i","inh"},
    }

    # nếu phụ âm không có trong dict thì giữ nguyên
    if phu_am not in PHU_AM_VAN:
        return word

    tap_van_hop_le = PHU_AM_VAN[phu_am]

    # nếu vần hợp lệ
    if van in tap_van_hop_le:
        return word

    # nếu không hợp lệ → tìm vần gần nhất theo độ dài
    van_moi = min(
        tap_van_hop_le,
        key=lambda v: abs(len(v) - len(van))
    )

    return phu_am + van_moi
def xu_ly_tu(word):
    word = xoa_ky_tu_lap(word)      
    word = sua_loi_chinh_ta(word)   
    word = change_alias(word)      
    return word
# =======================
# 4. CHẠY INPUT
# =======================
if __name__ == "__main__":
    error_text = input("Nhập câu cần xử lý: ")
    print("Kết quả:", process_error_text(error_text))
