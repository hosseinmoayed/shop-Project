




def Group_list(targetlist , split=4 , main_image = None):
    list_help = []
    list_asli = []
    n = 0
    for i in targetlist:
        n += 1
        list_help.append(i)
        if n % split == 0:
            list_asli.append(list_help)
            list_help = []
    if list_help != []:
        if main_image is not None:
            list_help.append({'image':main_image})
        list_asli.append(list_help)
    else:
        if main_image is not None:
            list_help.append({'image':main_image})
            list_asli.append(list_help)
    return list_asli
