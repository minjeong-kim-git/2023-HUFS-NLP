'''
작업에 따른 비용

d[i, j] = min(d[i-1], j] + insert_cost,
                d[i-1], j] + delete_cost,
               d[i-1], j] + substitution_cost
                 )
'''

def med(s1, s2):
    # 0으로 채워진 2차원 배열 current_row
    current_row = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # current_row의 칸에 비용을 저장
    for i in range(1, len(s1) + 1):
        current_row[i][0] = i
    
    for i in range(1, len(s2) + 1):
        current_row[0][i] = i
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i-1] == s2[i-1]:
               current_row[i][j] = current_row[i-1][j-1]
            else:
                # 추가, 삭제, 수정 비용 중 가장 작은 것을 current_row[i][j]에 저장
                current_row[i][j] = min(current_row[i-1][j], current_row[i][j-1], current_row[i-1][j-1]) + 1
    
    # 최소 비용 출력
    print(current_row[len(s1)][len(s2)])

# 사용자가 문자열을 입력하도록 함.
s1 = input("비교할 첫 번째 문자열을 입력해주세요: ")
s2 = input("비교할 두 번째 문자열을 입력해주세요: ")

# 입력한 문자열을 변수로 levenshtein 함수에 적용함.
# debug = True에 따라 행렬이 표시됨.
med(s1, s2)