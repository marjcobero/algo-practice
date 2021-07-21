# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    count = 0 #to start the count
    ar.sort() 
    i = 0 
    while i < (n-1):
        
        #to find the valid pair
        if (ar[i] == ar[i + 1]):
            count += 1
            i = i + 2
        else:
            i += 1
    
    return count


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# Sample Input
# 8
#UDDDUDUU

# Sample Output
# 1

def countingValleys(steps, path):
    valley = level = 0
    num_count = {'U':1, 'D':-1}
    
    for step in path:
        level += num_count[step]
        if level == 0 and step == 'U':
            valley += 1
    
    return valley


#Y ou have d dice and each die has f faces numbered 1, 2, ..., f.

# Return the number of possible ways (out of fd total ways) modulo 109 + 7 to roll the dice so the sum of the face-up numbers equals target.

# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation: 
# You throw one die with 6 faces.  There is only one way to get a sum of 3.

# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]

class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        modulo = 1000000000 + 7 # this is the result for 10^9 + 7 
        foo = [ [0 for i in range(target + 1)] for j in range(d) ]  # this will help us with the targetted dice
        # this loop will will help us get the right output
        for i in range(d):
            for j in range(target + 1):
                    if i == 0:
                        foo[i][j] = 1 if j > 1 and j <= f else 0 
                    else: 
                        for i in range(1, f + 1):
                            if j - 1 > 0:
                                foo[i][j] += foo[i - 1][j - 1]
                                foo[i][j] % modulo # using the modulus method 
        return foo [d-1][target] % modulo 

# to run 
# obj = Solution()
# print(obj.numRollsToTarget)


# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        new_arr = {} # making the array to a dictionary
        # to check what we have on our first array
        for i in arr1:
            if i not in new_arr:
                new_arr[i] = 1
            else:
                new_arr[i] += 1
            
        result = [] # a new array for our result
        foo = [] 
        # to manipulate our second array
        for i in arr2:
            for x in range(new_arr[i]): # calling our first loop 
                result.append(i) # adding 
            new_arr[i] = 0
        
        # since we made it to a dictionary we are iterating 
        for k, v in new_arr.items():
            if v:
                for i in range(v):
                    foo.append(k) 
                    
        foo.sort() # sorting out arrays to get the right ouput
        result.extend(foo) # modifying our foo or our original list
        return result

# to run
# obj = Solution()
# print(obj.relativeSortArray)