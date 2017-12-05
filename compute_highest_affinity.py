
# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    dict_1 = {}
    dict_2 = {}
 
    index_name = []
    for index in range(0,len(site_list)):
            
        if site_list[index] not in dict_1:
            index_name.append(site_list[index])
            dict_1[site_list[index]] = [user_list[index]]
            dict_2[site_list[index]] = {}
        else:
            dict_1[site_list[index]].append(user_list[index])

    for e in index_name:
        for i in range(0,len(index_name)):
            if e != index_name[i]:
                dict_2[e][index_name[i]] = 0


    for i in range(0,len(index_name)):
        for k in range(0,len(index_name)):
            if index_name[i] != index_name[k]:
                count = 0
                for e in dict_1[index_name[i]]:
                    if e in dict_1[index_name[k]]:
                        count = count + 1;
                dict_2[index_name[i]][index_name[k]] = count;

    position_1 = ""
    position_2 = ""
    max = 0
    for i in range(0,len(index_name)):
        for j in range(0,len(index_name)):
            if index_name[i] != index_name[j]:
                if dict_2[index_name[i]][index_name[j]] > max:
                    max = dict_2[index_name[i]][index_name[j]]
                    position_1 = index_name[i]
                    position_2 = index_name[j]

    list = [position_1,position_2]
    final = sorted(list)
    return(final[0],final[1])
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo").
  

