def find_num_sol(step_pos, n):
    dic_sol = {n:1}
    start = True

    while start:
        ##print('while jadid')
        dict2 = dic_sol.copy()
        for key in dic_sol:
            #print('key = ', str(key))
            i = 0
            for step in step_pos:
                #print('step=', str(step))
                a = key - step
                #print('adade jadid=', str(a))
                if a < 0 :
                    i +=1
                    continue
                
                elif a not in dict2:
                    ##print('dar surat Nabudan a')
                    dict2[a] = dict2[key]
                    #print(dict2)
                else:
                    ##print('dar surat budan a')
                    dict2[a] += dict2[key]
                    #print(dict2)
            else:
                if key > 0 :
                    del dict2[key]
        else:
            dic_sol = dict2.copy()
            ##print(dic_sol)
            if len(dic_sol) == 0:
                start = False
            elif len(dic_sol) == 1 and dic_sol.get(0):
                start = False
    return dic_sol