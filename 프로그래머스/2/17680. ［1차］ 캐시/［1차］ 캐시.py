def flow(arr):
    for k in arr.keys():
        arr[k] += 1
    return arr

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    
    cache = {}
    time = 0
    
    for city in cities:
        city = city.lower()
        
        if city not in cache: # miss
            if len(cache) < cacheSize:
                cache[city] = 0
            
            else:
                m = max(cache.values())
                for k, v in cache.items():
                    if v == m:
                        cache.pop(k)
                        cache[city] = 0
                        break
            time += 5
        
        else: # hit
            cache[city] = 0
            time += 1
        
        for k in cache.keys():
            cache[k] += 1

    return time