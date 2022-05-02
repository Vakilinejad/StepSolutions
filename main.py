def find_num_sol(step_pos, n):
    dic_sol = {n:1}
    start = True

    while start:
        dict2 = dic_sol.copy()
        for key in dic_sol:
            i = 0
            for step in step_pos:
                a = key - step
                if a < 0 :
                    i +=1
                    continue
                
                elif a not in dict2:
                    dict2[a] = dict2[key]
                else:
                    dict2[a] += dict2[key]
            else:
                if key > 0 :
                    del dict2[key]
        else:
            dic_sol = dict2.copy()
            if len(dic_sol) == 0:
                start = False
            elif len(dic_sol) == 1 and dic_sol.get(0):
                start = False
    return dic_sol