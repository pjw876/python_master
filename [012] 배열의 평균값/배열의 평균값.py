def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer

# 다른 사람의 풀이
# numpy를 사용하는 방법도 있다!
# import numpy as np
# def solution(numbers):
#     # mean은 numpy에서 평균을 뜻함  
#     return np.mean(numbers)