def solution(stones):
    stones = list(stones)
    times = 0
    for i in range(len(stones)-1):
        if stones[i] == stones[i+1]:
            times += 1
    return times
     

print(solution("RGBRGBRGGB"))