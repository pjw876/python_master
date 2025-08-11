def solution(n):
    return sum(range(2, n+1, 2))


# 다른 방법
# # n까지의 숫자 중 짝수만을 모두 더하기
# def solution(n):
#     # answer 초기 값 0으로
#     answer = 0
#     # n까지의 짝수만을 for문을 돌면서 각각 더하여 answer에 저장
#     for i in range(2, n+1, 2):
#         answer += i
#     return answer