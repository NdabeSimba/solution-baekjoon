import sys
input = sys.stdin.readline

N = int(input())
count = 1
mov_name = 666

while count != N:
    mov_name += 1
    if '666' in str(mov_name):
        count += 1
    
print(mov_name)

def movie_name(n):
    count = 0
    mov_name = 666

    while True:

        if '666' in str(mov_name):
            count += 1

        if count == n:
            return mov_name
        
        mov_name += 1

N = int(input())
print(movie_name(N))