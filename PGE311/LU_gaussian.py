import numpy as np
import scipy as sc

def forward_elimination_upper(A, b):
    m, n = A.shape

    if m != n:
        print('Should be a  square matrix.')

    for i in range(m-1):
        # print('i',i)
        if np.abs(A[i,i]) > 1e-15:  #Check to see if the matrix is too big

            for j in range(i+1,n):
                # print('j',j)
                # print('A[j,i]',A[j,i])
                c = A[j, i] / A[i,i]
                A[j,:] = A[j, :] - c*A[i,:]
                b[j] = b[j] - c*b[i]


        else:
            print(f'Pivot element i={i} is zero')
            break
    # print('A\n',A)
    # print('b\n',b)
    # print('LOWER DONE')
    return A, b


# def forward_elimination_lower(A,b):
#     m, n = A.shape
#
#     if m != n:
#         print('Should be a  square matrix.')
# #m-1,0,-1
#     for i in range(m-1,0,-1):
#         if np.abs(A[i,i]) > 1e-15:  #Check to see if the matrix is too big
#
#             for j in range(i-1,-1,-1):
#
#                 c = A[j,i] / A[i, i]
#                 A[j,:] = A[j, :] - c*A[i,:]
#                 b[j] = b[j] - c*b[i]
#                 print('A\n', A)
#
#
#         else:
#             print(f'Pivot element i={i} is zero')
#         #     break
#     # print('A\n',A)
#     # print('b\n',b)
#     # print('UPPER DONE')
#     return (A, b)

def forward_elimination_lower(A,b):


    U,b = forward_elimination_upper(np.copy(A),b)
    inv_matrix = np.linalg.inv(np.copy(U))
    lower_matrix = A@inv_matrix
    return lower_matrix

def back_substitution(A,b):
    n = len(b)

    x = np.zeros(b.shape)
    x[n-1] = b[n-1]/A[n-1,n-1]

    for i in range(n-2,-1,-1):
        s = 0
        for j in range(i+1,n):
            s = s + A[i,j] * x[j]
        x[i] = (b[i]-s)/A[i,i]

    return x


def gaussian_elimination(A,b):

    A,b = forward_elimination_lower(A,b)
    x = back_substitution(A,b)

    return x
K = np.array([[10.,2,-1],[-3,-6,2],[1,1,5]])
l = np.array([27,-61.5,-21.5])

def lu_factor(A,b):

    A_upper, b_upper = forward_elimination_upper(np.copy(A), np.copy(b))
    A_lower = forward_elimination_lower(np.copy(A), np.copy(b))

    return A_upper,A_lower

K = np.array([[10.,2,-1],[-3,-6,2],[1,1,5]])
l = np.array([27,-61.5,-21.5])
#forward_elimination_lower1(K,l)
U,L = (lu_factor(K,l))
print('MY UPPER\n', U)
print('MY LOWER\n', L)
print('Mult \n',L@U)
print('')
# NOT WORKING PROPERLY
P,L,U = sc.linalg.lu(K)
print('SCIPY LOWER\n', L)
print('SCIPY UPPER\n',U)

# print(forward_elimination_upper(K,l))
# print(forward_elimination_lower(K,l))


def forward_sub(L,b):
    m,n = L.shape
    d = np.zeros(b.shape)
    d[0] = b[0]/ L[0,0]

    if m != n:
        print('forward_substitution: please provide a square matrix')

    for i in range(1,n):
        s = 0
        for j in range(0,i):
            s += L[i,j]*d[j]
        d[i] = (b[i] -s)/ L[i,i]

    print(d)
    return d


# A = np.array([[-2,1,1],[4,-6,6],[-6,-3,-10]])
# b = np.array([12,18,-6])
#
# P,L,U = sc.linalg.lu(A)
# #print(L,U)
#
# d = forward_sub(L,b)
# x = back_substitution(U,d)
# #print('HERE',x)