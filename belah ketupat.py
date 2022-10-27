# (A)

# for i in range(4):
#     for j in range(2):
#         print('*' )
#     for j in range(2):
#         print('*' )

# (B)

# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end="")
#     for j in range(i):
#         print('*',end="")
#     for j in range(i+1):
#         print('*', end='')
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print('', end='')
#     for j in range(i,n-1):
#         print('*',end='')
#     for j in range(i,n):
#         print('*',end='')
#     print()

# (C)

# a = input('? ')
# a=int(a)
# for i in range(a):
#     print(' '*(a-i-1)+'*'*(i+1))
# for j in range(a-1,0,-1):
#     print(' '*(a-j)+'*'*(j))

# (D)

print('    *')
print('   * *')
print('  * * *')
print(' * * * *')
print('* * * * *')
print(' * * * *')
print('  * * *')
print('   * *')
print('    *')