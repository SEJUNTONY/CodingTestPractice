def solution(new_id):
    # 기본 조건
    i = 0
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    length = len(new_id)
    q = 0
    for i in range (length) :
        if q >= len(new_id) :
            break
        
        if (new_id[q].isdigit() == False) and (new_id[q].isalpha() == False) :
            if new_id[q] == "-" :
                q += 1
            elif new_id[q] == "_" :
                q += 1
            elif new_id[q] == "." :
                q += 1
            elif new_id[q] == " " :
                q += 1
            else :
                new_id = new_id[:q] + "" + new_id[q+1:]

        else :
            q += 1
    
    if new_id == "" :
        new_id = " "

    # 3단계
    i = 0 # Reset
    q = 0 # Reset
    length = len(new_id) # Reset
    for i in range (length) :
        if q >= len(new_id) :
            break
        if q == 0 :
            if new_id[q] == "." :
                if len(new_id) == 1 :
                    break
                elif new_id[q+1] == "." :
                    new_id = new_id[:q] + "" + new_id[q+1:]
        if q >= 0 :
            if new_id[q] == "." :
                if q == len(new_id)-1 :
                    new_id = new_id[:q+1]
                elif new_id[q+1] == "." :
                    new_id = new_id[:q] + "" + new_id[q+1:]

        q += 1
    
    if new_id == "" :
        new_id = " "

    # 4단계
    i = 0 # Reset
    q = 0 # Reset
    length = len(new_id) # Reset
    if new_id[0] == "." :
        new_id = new_id[1:]
    for i in range (len(new_id)) :
        if new_id[len(new_id)-1] == "." :
            new_id = new_id[:len(new_id)-1]
        else :
            break

    if new_id == "" :
        new_id = " "

    # 5단계
    i = 0 # Reset
    q = 0 # Reset
    length = len(new_id) # Reset
    for i in range (length) :
        if q >= len(new_id) :
            break
        if new_id[q] == " " :
            new_id = new_id[:q] + "a" + new_id[q+1:]
        q += 1
    

    # 6단계
    i = 0 # Reset
    q = 0 # Reset
    length = len(new_id) # Reset
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        q = 14
        for i in range(16) :
            if new_id[q] == "." :
                new_id = new_id[:q]
                q -= 1
            else :
                break
    
    # 7단계
    i = 0 # Reset
    q = 0 # Reset
    length = len(new_id) # Reset
    if len(new_id) == 1 :
        new_id = new_id[0] + new_id[0] + new_id[0]
    if len(new_id) == 2 :
        new_id = new_id[0] + new_id[1] + new_id[1]

    answer = new_id
    return answer

new_id = "=.="
print(solution(new_id))