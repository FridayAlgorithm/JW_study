def installrouter_len(first, last, c):
    while first <= last:
        mid = (first + last) // 2
        
        cnt =1
        installed = home[0]
        for i in range(len(home)):
            if(home[i] - installed) >= mid:
                cnt += 1
                installed = home[i]

                
        if cnt >= c:
            router_len.append(mid)
            first = mid + 1
        else:
            last = mid -1
            
n, c = map(int, input().split())

home =[]
for i in range(n):
    home.append(int(input()))
    
home.sort()

router_len = []
installrouter_len(1, home[n-1] - home[0], c)

print(max(router_len))





