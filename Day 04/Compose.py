# 초성이 되는 자음 목록
choseong_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성이 되는 모음 목록
joongseong_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성의 경우 자음도 되고, 이중자음도 가능하며 없을 수도 있음.(공백)
jongseong_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def compose(cho, joong, jong):
    # 유효성 검사
    if cho not in choseong_list:
        raise ValueError('초성이 유효하지 않습니다.')
    if joong not in joongseong_list:
        raise ValueError('중성이 유효하지 않습니다.')
    if jong not in jongseong_list:
        raise ValueError('종성이 유효하지 않습니다.')
    cho_idx = choseong_list.index(cho)
    joong_idx = joongseong_list.index(joong)
    jong_idx = jongseong_list.index(jong)

    #한글 자모 조합
    letter = chr(0xAC00 + cho_idx * 21 * 28 + joong_idx * 28 + jong_idx)
    return letter

cho = input('자모를 결합할 문자의 초성을 입력허세요: ')
joong = input('자모를 결합할 문자의 중성을 입력허세요: ')
jong = input('자모를 결합할 문자의 종성을 입력허세요: ')

letter = compose(cho, joong, jong)
print('결과:', letter)