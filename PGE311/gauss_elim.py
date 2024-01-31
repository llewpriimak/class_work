import numpy as np
from timeit import default_timer as timer

def forward_elimination(A, b):
    m, n = A.shape

    if m != n:
        print('Should be a  square matrix.')

    for i in range(m-1):

        if np.abs(A[i,i]) > 1e-15:  #Check to see if the matrix is too big

            for j in range(i+1,n):
                c = A[j, i] / A[i,i]
                A[j,:] = A[j, :] - c*A[i,:]
                b[j] = b[j] - c*b[i]

        else:
            print(f'Pivot element i={i} is zero')
            break
    # print('A\n',A)
    # print('b\n',b)

    return (A, b)


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


# A = np.array([[-3,2,-1],[6,-6,7],[3,-4,4]])
# b = np.array([-1,-7,-6])
#
# print(back_substitution(A,b))

def gaussian_elimination(A,b):

    A,b = forward_elimination(A,b)
    x = back_substitution(A,b)

    return x


# Test the code on the 4 by 4 example
# A = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[2, 0, 4, 5],[0, 4, 5, 6]])
# b = np.array([1,3,5,7])
K = np.array([[-8,1,-2],[2,-6,-1],[-3,-1,7]])
l = np.array([-20,-38,-34])
x= gaussian_elimination(K,l)


print('x\n',x)


# check if the result is correct
print('\nCheck Ax-b:', np.matmul(K,x)-l)
print('L2 norm of Ax-b:', np.linalg.norm(np.matmul(K,x)-l))


def time_it():
    # Example with some random numbers
    N = 10000
    # Generate A and b with random integers in given ranges [low,high]
    A = np.random.rand(N, N)
    b = np.random.rand(N, 1)

    start = timer()
    x = gaussian_elimination(A, b)
    end = timer()

    t = end - start
    print(f"\nGE took {t:.4f} seconds.")

    # now time np.linalg.solve function
    start = timer()
    x = np.linalg.solve(A, b)
    end = timer()

    t = end - start
    print(f"\nnp.linalg.solve took {t:.4f} seconds.")
#time_it()
# For N = 1000
# Gaussian Elimination took 4.2394 seconds
# np.linalg.solve took 0.0158 seconds.
# For N = 5000
# Gaussian Elimination took 194.3856 seconds
# np.linalg.solve took 0.8973 seconds.
# For N = 10000
# Gaussian Elimination took 1192.0449 seconds
# np.linalg.solve took 5.9321 seconds.



###
# Testing LU factorization done by hand
###

L = np.array([[1,0,0], [-2,1,0],[-1,1,1]])
U = np.array([[-3,2,-1],[0,-2,5],[0,0,-2]])
A = np.array([[-3,2,-1],[6,-6,7],[3,-4,4]])


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
b = np.array([-1,-7,-6])


I = np.eye(3)
# # first column of inverse
# b = I[:,0]
# d = forward_sub(L,b)
# x1 = back_substitution(U,d)
# print(x1)
# # second column of inverse
# b = I[:,1]
# d = forward_sub(L,b)
# x2 = back_substitution(U,d)
# print(x2)
# # Third column of inverse
# b = I[:,2]
# d = forward_sub(L,b)
# x3 = back_substitution(U,d)
# print(x3)

# m,n = A.shape
# Ainv = np.zeros(A.shape)
# for i in range(n):
#     b = I[:, i]
#     d = forward_sub(L, b)
#     xi = back_substitution(U, d)
#     print(xi)
#     Ainv[:,i] = xi
# print(A@Ainv)

# This helper does the actual row pivoting
def fepp_helper(A,b,i):


    find_index = np.argmax(np.absolute(A[i:,i])).item() + i
    A[[find_index, i]] = A[[i,find_index]]
    b[find_index] , b[i] = b[i] , b[find_index]

    return A,b


def forward_elimination_partial_pivot(A,b):
    m, n = A.shape

    if m != n:
        print('Should be a  square matrix.')

    for i in range(m-1):

        if np.abs(A[i,i]) > 1e-15:  #Check to see if the matrix is too big
            A, b = fepp_helper(A, b, i)

            for j in range(i+1,n):
                #print('Max',np.max(np.absolute(A[:,i])))
                if A[i,i] < np.max(np.absolute(A[:,i])):
                    #

                    c = A[j, i] / A[i,i]
                    A[j,:] = A[j, :] - c*A[i,:]
                    b[j] = b[j] - c*b[i]
                else:
                    c = A[j, i] / A[i,i]
                    A[j,:] = A[j, :] - c*A[i,:]
                    b[j] = b[j] - c*b[i]

        else:
            print(f'Pivot element i={i} is zero')
            break
    print('A\n',A)
    print('b\n',b)

    return (A, b)

K = np.array([[2,-6,-1],[-8,1,-2],[-3,-1,7]])
l = np.array([-38,-20,-34])

#forward_elimination_partial_pivot(K,l)


