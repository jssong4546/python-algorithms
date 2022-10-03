# https://www.acmicpc.net/problem/2512

regionCount = int(input())
budgetList = list(map(int, input().split(' ')))
countryBudget = int(input())

def totalDistBudget(val):
    sum = 0
    
    for budget in budgetList:
        if val <= budget:
            sum += val
        else:
            sum += budget
        
    return sum

low = 0
high = max(budgetList)
maxBudget = 0

while low <= high:
    mid = (low + high) // 2
    
    total = totalDistBudget(mid)
    
    if total <= countryBudget:
        maxBudget = mid
        low = mid + 1
    else:
        high = mid - 1
        
print(maxBudget)
