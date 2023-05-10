def solution(s):
    left = 0
    right = 0
    arr = list(s)
    if (arr[0] == ")") or (arr[len(arr)-1] == "("):
        return False
    else:
        while len(arr) > 0 :
            if (arr.pop() == ")"):
                right += 1
            else:
                right -= 1
        
            if right < 0:
                return False
    
    if (right == 0):
        return True
    else:
        return False
                