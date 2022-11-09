#Дан список А размера N и целые числа размера K и L(1 < K < L < N). Переставить в
#обратном порядке элементы списка, расположеные между элементами AK и AL, не включая эти
#элементы

from random import sample
n, k, l = [int(input('Введите значения "N, K, L" через Enter:\n')) for i in range (3)]
lst = sample(range(1, 100), n)
l -= 1
print(*lst, sep = 'l')
lst[k:l] = lst[k:l][::-1]
print(*lst, sep = 'l')

