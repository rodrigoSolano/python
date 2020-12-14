def sort_me(courses): 
    data = list()
    for course in courses:
        temp = course.split("-")
        data.append(temp[1]+"-"+temp[0])
    data = sorted(data)
   
    data_1 = list()
    for dato in data:
        temp = dato.split("-")
        data_1.append(temp[1]+"-"+temp[0])

    return data_1

print(sort_me(['aeb-1305', 'site-1305', 'play-1215', 'web-1304', 'site-1304', 'beb-1305']))