@ -0,0 +1,81 @@
def remove_reduntdant_char(text):
    """
    Loại bỏ các phụ âm ghép đầu từ trong chuỗi đầu vào.
    text: str
    return: str, list, list
    """
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
    """
    Chuyển đổi các ký tự có dấu thành không dấu.
    alias: str
    return: str
    """
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
    # Chuẩn hóa dữ liệu
    str_ = alias.lower()
    process, char_deleted, indexs = remove_reduntdant_char(str_)
    # Thay thế các ký tự có dấu thành không dấu
    # Ưu tiên thay thế các trường hợp dài nhất trước
    for length in range(4, 1, -1):
        for i in range(len(process) - length + 1):
            key = process[i:i+length]
            if key in telex_map:
                process = process[:i] + telex_map[key] + process[i+length:]
                return "".join(char_deleted) + process
    # Nếu không có trường hợp đặc biệt, kiểm tra các trường hợp 2 ký tự
    for key in telex_map:
        if process == key:
            process = telex_map[key]
            break
    return "".join(char_deleted) + process

def process_error_text(error_text: str) -> str:
    """
    Xử lý một câu có nhiều từ, áp dụng change_alias cho từng từ.
    error_text: str
    return: str
    """
    text = error_text.split(" ")
    processed_text = []

    for word in text:
        processed_text.append(change_alias(word))

    return " ".join(processed_text)

if __name__ == "__main__":
    error_text = input("Nhập câu cần xử lý: ")
    result = process_error_text(error_text)
    print(result)
