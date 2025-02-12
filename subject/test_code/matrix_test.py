import numpy as np
import random

def TEST_MAXTRIX_DOT(function):
    num_tests = 10
    max_size = 5
    count = 0 

    for _ in range(num_tests):
        # 랜덤 행렬 크기 생성
        rows_a = random.randint(1, max_size)
        cols_a = random.randint(1, max_size)
        rows_b = cols_a  # 행렬 곱셈이 가능하도록 크기 설정
        cols_b = random.randint(1, max_size)
        
        # 랜덤 행렬 생성
        A = np.random.rand(rows_a, cols_a)
        B = np.random.rand(rows_b, cols_b)
        
        # numpy의 dot과 사용자 정의 함수 결과 비교
        expected = np.dot(A, B)
        result = function(A, B)
        
        # 결과가 다르면 실패 반환
        if not np.array_equal(expected, result):
            print(f"Test Fail !! : Matrix shape A{A.shape}, B{B.shape}")
            print("Expected :\n", expected)
            print("Result :\n", result)
        else:
            count += 1
    
    print(f"TEST result {count} / {num_tests} Pass")