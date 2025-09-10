def video_zip(N, video, ofsr, ofsc): 
    color = set()

    for row in range(ofsr, ofsr+N): 
        for col in range(ofsc, ofsc+N): 
            color.add(video[row][col])
            if len(color) == 2:
                result.append('(')
                video_zip(N//2, video, ofsr, ofsc)
                video_zip(N//2, video, ofsr, ofsc+N//2)
                video_zip(N//2, video, ofsr+N//2, ofsc)
                video_zip(N//2, video, ofsr+N//2, ofsc+N//2)
                result.append(')')
                break
        else: 
            continue
        break
    else: 
        result.append(color.pop())

N = int(input())
video = list(input() for _ in range(N))
result = []
video_zip(N, video, 0, 0)
print(''.join(result))