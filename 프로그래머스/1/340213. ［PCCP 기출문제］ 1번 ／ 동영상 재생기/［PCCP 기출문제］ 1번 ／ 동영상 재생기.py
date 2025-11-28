def solution(video_len, pos, op_start, op_end, commands):
    m, s = map(int, video_len.split(":"))
    total_video_len = m * 60 + s
    
    m, s = map(int, pos.split(":"))
    total_pos = m * 60 + s
    
    m, s = map(int, op_start.split(":"))
    total_op_start = m * 60 + s
    
    m, s = map(int, op_end.split(":"))
    total_op_end = m * 60 + s
    
    
    for command in commands:
        if total_op_start <= total_pos and total_pos <= total_op_end:
                total_pos = total_op_end
        
        if command == "prev":
            if total_pos - 10 < 0:
                total_pos = 0
            else:
                total_pos -= 10
            
        elif command == "next":
            if total_pos + 10 > total_video_len:
                total_pos = total_video_len
            else:
                total_pos += 10
                
        if total_op_start <= total_pos and total_pos <= total_op_end:
                total_pos = total_op_end
    
    answer = ''
    m = total_pos // 60
    n = total_pos % 60
    answer = f"{m:02}:{n:02}"

    return answer