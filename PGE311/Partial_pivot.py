import numpy as np


# This is a script to run both a partial pivot, forward elimination
# and back substitution on a system of linear algebra equations
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

def gaussian_elimination_partial_pivote(A,b):

    A,b = forward_elimination_partial_pivot(A,b)
    x = back_substitution(A,b)

    return x


# K = np.array([[2,-6,-1],[-8,1,-2],[-3,-1,7]])
# l = np.array([-38,-20,-34])
# A = np.array([[2,-6,-1],[-3,-1,7],[-8,1,-2]])
# b = np.array([-38,-34,-20])
A = np.array([[0.55,0.30,0.15],[0.25,0.45,0.30],[0.25,0.20,0.55]])
A_t = np.transpose(A)
b = np.array([4900,5800,5700])
print(gaussian_elimination_partial_pivote(A_t,b))
# Z,b  = forward_elimination_partial_pivot(A,b)
#
# print(np.linalg.det(Z))