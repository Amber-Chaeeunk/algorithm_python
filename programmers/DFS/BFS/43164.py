from collections import defaultdict

def dfs(dic, route, n):
    if len(route) == n+1:
        return route
    for i, r in enumerate(dic[route[-1]]):
        dic[route[-1]].pop(i)
        answer = dfs(dic, route+[r], n)
        dic[route[-1]].insert(i, r)
        if answer:
            return answer

def solution(tickets):
    dic = defaultdict(list)
    for key, value in tickets:
        dic[key].append(value)
    for key in dic.keys():
        dic[key].sort()
        
    answer = dfs(dic, ['ICN'], len(tickets))
    return answer