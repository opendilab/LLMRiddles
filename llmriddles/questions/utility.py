def word_reverse_text(input_text, lang='cn'):
    if lang == 'cn':
        user_text = input_text[::-1]
    else:
        words = input_text.split()
        words.reverse()
        user_text = ' '.join(words)
    return user_text


def count_words(text: str, contain_punctuation: bool = False):
    chinese_words = []
    english_words = []
    other_words = []
    temp_english_words = []
    for char in text:
        if '\u4e00' <= char <= '\u9fff':
            chinese_words.append(char)
            if len(temp_english_words) > 0:
                english_words.append(''.join(temp_english_words))
                temp_english_words = []
        else:
            if char.isalpha():
                temp_english_words.append(char)
            else:
                if len(temp_english_words) > 0:
                    english_words.append(''.join(temp_english_words))
                    temp_english_words = []
                other_words.append(char)
    if contain_punctuation:
        return len(chinese_words) + len(english_words) + len(other_words)
    else:
        return len(chinese_words) + len(english_words)
