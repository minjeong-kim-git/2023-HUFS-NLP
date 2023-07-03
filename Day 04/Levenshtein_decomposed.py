import sys
from Levenshtein_jamo import levenshtein_jamo

# 초성이 되는 자음 목록
choseong_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성이 되는 모음 목록
joongseong_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성의 경우 자음도 되고, 이중자음도 가능하며 없을 수도 있음.(공백)
jongseong_list = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def decompose(word):
    word_list = []
    for letter in list(word.strip()):
        if '가' <= letter <= '힣':
            char1 = (ord(letter) - ord('가')) // 588
            # 중성은 28가지 종류
            char2 = ((ord(letter) - ord('가')) - (588 * char1)) // 28
            char3 = ((ord(letter) - ord('가')) - (588 * char1)) - 28 * char2
            # 분리한 자모를 word_list에 추가
            # 초성, 중성, 종성을 각각 저장
            word_list.append([choseong_list[char1], joongseong_list[char2], jongseong_list[char3]])
        else:
            word_list.append([letter])
    return word_list

def decompose_sentence(sentence):
    decomposed = []
    for word in sentence.split():
        decomposed_word = decompose(word)
        decomposed.append([decomposed_word])
    return decomposed

sentence1 = input("비교할 첫 번째 문장을 입력하세요: ")
sentence2 = input("비교할 두 번째 문장을 입력하세요: ")

decomposed1 = decompose_sentence(sentence1)
decomposed2 = decompose_sentence(sentence2)

total_distance = 0
for word1, word2 in zip(decomposed1, decomposed2):
    word_distance = 0
    for jamo1, jamo2 in zip(word1, word2):
        jamo_distance = levenshtein_jamo(jamo1, jamo2)
        word_distance += jamo_distance
    total_distance += word_distance

print('Levenshtein 거리:', total_distance)
print('해체된 문장1', decomposed1)
print('해체된 문장2', decomposed2)