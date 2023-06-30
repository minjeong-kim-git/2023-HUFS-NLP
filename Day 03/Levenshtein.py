'''
작업에 따른 비용

d[i, j] = min(d[i-1], j] + insert_cost,
                d[i-1], j] + delete_cost,
               d[i-1], j] + substitution_cost
                 )
'''

def levenshtein(s1, s2, debug = False):
    if len(s1) < len(s2):
        return levenshtein(s1, s2, debug)
    # 두 번째로 입력한 문자열이 없다면?
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i+1]
        for j, c2 in enumerate(s2):
            # 추가, 삭제, 수정에 따른 비용 합산
            insertions = previous_row[j+1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            # 각 비용 중 가장 작은 비용을 current_now에 추가
            current_row.append(min(insertions, deletions, substitutions))
        if debug:
            print(current_row[1:])
        
        # current_now의 데이터를 previous_row에 저장함.
        previous_row = current_row
    
    # 가장 마지막의 원소를 불러오도록 함.
    return previous_row[-1]

# 사용자가 문자열을 입력하도록 함.
s1 = input("비교할 첫 번째 문자열을 입력해주세요: ")
s2 = input("비교할 두 번째 문자열을 입력해주세요: ")

# 입력한 문자열을 변수로 levenshtein 함수에 적용함.
# debug = True에 따라 행렬이 표시됨.
levenshtein(s1, s2, debug = True)