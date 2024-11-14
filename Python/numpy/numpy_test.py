import numpy as np

# arr = np.arange(10)
# arr = arr.reshape(5, 2)

# print("행렬의 모양 : ", arr.shape)
# print("행렬의 축 개수 : ", arr.ndim)
# print("행렬 내 원소의 개수 : ", arr.size)

# arr2 = np.arange(20).reshape(4,5)
# print(arr2.dtype)
# print(type(arr2))

# arr3 = np.array([0,1,2,3,4,'5'])
# print(arr3.dtype)
# arr4 = np.array(['1','2','3','4','5'])
# print(arr4.dtype)

# arr = np.arange(16).reshape(4,4)
# arr * 2
# arr + 2
# arr2 = np.array([1,2,3,4])
# arr3 = np.array([[1],[2],[3],[4]])
# print(arr + arr2)
# print(arr + arr3)

# arr = np.arange(9).reshape(3,3)
# print(arr[:,2:])
# print(arr[0,:1])

# # 0에서 1사이의 실수형 난수 하나를 생성합니다. 
# print(np.random.random())   
# # 0~9 사이 1개 정수형 난수 하나를 생성합니다. 
# print(np.random.randint(0,10))   
# # 리스트에 주어진 값 중 하나를 랜덤하게 골라줍니다.
# print(np.random.choice([0,1,2,3,4,5,6,7,8,9]))  

# # 무작위로 섞인 배열을 만들어 줍니다. 
# print(np.random.permutation(10))   
# print(np.random.permutation([0,1,2,3,4,5,6,7,8,9]))

# # 이것은 정규분포를 따릅니다.
# # 평균(loc), 표준편차(scale), 추출개수(size)를 조절해 보세요.
# print(np.random.normal(loc=0, scale=1, size=5))    

# # 이것은 균등분포를 따릅니다. 
# # 최소(low), 최대(high), 추출개수(size)를 조절해 보세요.
# print(np.random.uniform(low=-1, high=1, size=5))  

# A = np.arange(24).reshape(2,3,4)
# print("A:", A)               # A는 (2,3,4)의 shape를 가진 행렬입니다. 
# print("A의 전치행렬:", A.T)            
# print("A의 전치행렬의 shape:", A.T.shape) # A의 전치행렬은 (4,3,2)의 shape를 가진 행렬입니다.

# print(np.random.rand(3,3))
# print(np.random.randint(1, 100, (3,3)))


# -----------------------------------------------------------

# def numbers():
#     X = []
#     number = input("Enter a number (<Enter key> to quit)") 
#     # 하지만 2개 이상의 숫자를 받아야 한다는 제약조건을 제외하였습니다.
#     while number != "":
#         try:
#             x = float(number)
#             X.append(x)
#         except ValueError:
#             print('>>> NOT a number! Ignored..')
#         number = input("Enter a number (<Enter key> to quit)")
#     return X

# def main():
#     nums = numbers()       
#     num = np.array(nums) 
#     print("합", num.sum())
#     print("평균값",num.mean())
#     print("표준편차",num.std())
#     print("중앙값",np.median(num))   

# main()

# -----------------------------------------------------------

from PIL import Image, ImageColor
import os
image_path = os.getenv("HOME") + "/programming/AI/AIFFEL/AIFFEL_quest_cr/Python/practice/newyork.png"
image = Image.open(image_path)
print(image_path)
print(type(image))
W, H = image.size
print((W, H))
print(image.format)
print(image.size)
print(image.mode)

cropped_image_path = os.getenv("HOME") + "/programming/AI/AIFFEL/AIFFEL_quest_cr/Python/practice/cropped_img.png"
image.crop((30,30,100,100)).save(cropped_image_path)
print("저장 완료!")

image_arr = np.array(image)
print(type(image))
print(type(image_arr))
print(image_arr.shape)
print(image_arr.ndim)

print(image_arr)