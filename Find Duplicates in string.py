from collections import defaultdict

def find_duplicates(A):
    count = defaultdict(int)
    for i in range(len(A)):
        count[A[i]] += 1
    
    for it in count:
        if (count[it] > 1):
            print(it, ", count = ", count[it])
 
# Driver code
if __name__ == "__main__":
 
    A = "test string"
    find_duplicates(A)
 