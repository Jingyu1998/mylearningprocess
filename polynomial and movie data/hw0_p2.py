with open("IMDB-Movie-Data.csv","r") as f:
    data = []
    for line in f.readlines():
        line = line.strip()
        data.append([line])
#print(data)
#------------------重新將資料按行存成list
i = 0
while i < len(data):
    data[i] = data[i][0].split(",")
    i = i + 1
#print(data)

a = []
i = 0
while i < len(data):
    if data[i][5] == "2016":
        a.append(data[i])
    i = i + 1
#print(a)

b = []
c = []
i = 0
while i < len(a):
    b.append(a[i][1])
    c.append(float(a[i][7]))
    i = i + 1

#print(b)
#print(c)
bc_dic = dict(zip(b,c))
#print(bc_dic)
#print(sorted(bc_dic.items(),key=lambda item:item[1],reverse=True))
print("Top-3 movies with the highest ratings in 2016 is Dangal,Kimi no na wa,Koe no katachi")
print()
#-----------------------------------------------------------------------------------------------------
aa = []
i = 0
while i < len(data):
    if "Emma Watson" in data[i][4]:
        aa.append(data[i])
    i = i + 1
#print(aa)

b = []
c = []
i = 0
while i < len(aa):
    b.append(aa[i][4])
    c.append(float(aa[i][7]))
    i = i + 1

bc_dic = dict(zip(b,c))
#print(bc_dic)
#print(sorted(bc_dic.items(),key=lambda item:item[1],reverse=True))
print("The average rating of Emma Watson’s movies is %.3f"  %(sum(c)/len(c)))
print()
#----------------------------------------------------------------------------------------
actorr = []
revenue = []
i = 1
while i < len(data):
    actorr.append(data[i][4])
    revenue.append(data[i][9])
    i = i + 1
#-----------------------------將缺失值用-1補值
revenuee = []
i = 0
while i < len(revenue):
    if revenue[i] == '':
        revenuee.append(-1)
    else:
        revenuee.append(float(revenue[i]))
    i = i + 1
#print(revenuee)
#--------------------將actor字串用"|"切
i = 0
new_actorr = []
while i < len(actorr):
    new_actorr.append(actorr[i].split("|"))
    i = i + 1
#print(new_actorr)
#-------------------------移除某些字串的左空格
i = 0
while i < len(new_actorr):
    j = 0
    while j < len(new_actorr[i]):
        new_actorr[i][j] = new_actorr[i][j].lstrip(" ")
        j = j + 1
    i = i + 1
#print(new_actorr)
#創造清除重複演員的演員list
i = 0
nnew_actorr = []
while i < len(new_actorr):
    j = 0
    while j < len(new_actorr[i]):
        if new_actorr[i][j] not in nnew_actorr:
            nnew_actorr.append(new_actorr[i][j])
        j = j + 1
    i = i + 1
#print(nnew_actorr)
#-------------存哪些演員演過哪些片
actor_index = []
k = 0
while k < len(nnew_actorr):
    i = 0
    aactor_index = []
    while i < len(new_actorr):
        j = 0
        while j < len(new_actorr[i]):
            if new_actorr[i][j] == nnew_actorr[k]:
                aactor_index.append(i)
            j = j + 1
        i = i + 1
    actor_index.append(aactor_index)
    k = k + 1
#----------------------計算每一個演員的平均revenue
average_revenue = []
i = 0
while i < len(actor_index):
    j = 0
    temp = []
    while j < len(actor_index[i]):
        if revenuee[actor_index[i][j]] >= 0:
            temp.append(revenuee[actor_index[i][j]])
        j = j + 1
    if len(temp) == 0:
        average_revenue.append(0)
    else:
        average_revenue.append(sum(temp)/len(temp))
    i = i + 1
#print(average_revenue)

average_actor = dict(zip(nnew_actorr,average_revenue))
#print(average_actor)
#print(sorted(average_actor.items(),key=lambda item:item[1],reverse=True))
print("The actor generating the highest average revenue is Daisy Ridley and John Boyega")
print()
#----------------------------------------------------------------------------------------
i = 1
director = []
while i < len(data):
    if data[i][3] not in director:
        director.append(data[i][3])
    i = i + 1
#print(data)
#print(director)
#-------------------將所有與某位導演合作過的演員存成 list
i = 0
aactor = []
while i < len(director):
    actor = []
    k = 1
    while k < len(data):
        if data[k][3] in director[i]:
            actor.append(data[k][4])
        k = k + 1
    aactor.append(actor)
    i = i + 1
#print(director)
#print(aactor)
#--------------------將字串用"|"切
nnew_actor = []
i = 0
while i < len(aactor):
    j = 0
    new_actor = []
    while j < len(aactor[i]):
        new_actor.extend(aactor[i][j].split("|"))
        j = j + 1
    nnew_actor.append(new_actor)
    i = i + 1
#print(nnew_actor)
#-------------------------移除某些字串的左空格
i = 0
while i < len(nnew_actor):
    j = 0
    while j < len(nnew_actor[i]):
        nnew_actor[i][j] = nnew_actor[i][j].lstrip(" ")
        j = j + 1
    i = i + 1
#print(nnew_actor)
#---------------------移除list的重複項
i = 0
nnnnew_actor = []
while i < len(nnew_actor):
    j = 0
    nnnew_actor = []
    while j < len(nnew_actor[i]):
        if nnew_actor[i][j] not in nnnew_actor:
            nnnew_actor.append(nnew_actor[i][j])
        j = j + 1
    nnnnew_actor.append(nnnew_actor)
    i = i + 1
#print(nnnnew_actor)
#------------------------算每一位的導演合作過的演員數
i = 0
actor_count = []
while i < len(nnnnew_actor):
    actor_count.append(len(nnnnew_actor[i]))
    i = i + 1
#print(director)
#print(actor_count)
direc_actor = dict(zip(director,actor_count))
#print(sorted(direc_actor.items(),key=lambda item:item[1],reverse=True))
print("Top-3 directors who collaborate with the most actors is Ridley Scott, M. Night Shyamalan,"
      " Danny Boyle, Paul McGuigan, Paul W.S. Anderson")
print()
#----------------------------------------------------------------------------------------------------
genre = []
i = 1
while i < len(data):
    genre.append(data[i][2])
    i = i + 1
#字串用"|"切
i = 0
new_genre = []
while i < len(genre):
    new_genre.append(genre[i].split("|"))
    i = i + 1
#清除重複類型的類型list
nnew_genre = []
i = 0
while i < len(new_genre):
    j = 0
    while j < len(new_genre[i]):
        if new_genre[i][j] not in nnew_genre:
            nnew_genre.append(new_genre[i][j])
        j = j + 1
    i = i + 1
#print(nnew_genre)
#存每一位演員演過電影的類型
actor_genre = []
k = 0
while k < len(nnew_actorr):
    i = 0
    aactor_genre = []
    while i < len(new_actorr):
        j = 0
        while j < len(new_actorr[i]):
            if new_actorr[i][j] == nnew_actorr[k]:
                aactor_genre.extend(new_genre[i])
            j = j + 1
        i = i + 1
    actor_genre.append(aactor_genre)
    k = k + 1
#print(actor_genre)
#清除每位演員演過的重複類型
i = 0
actor_genreee = []
while i < len(actor_genre):
    j = 0
    actor_genree = []
    while j < len(actor_genre[i]):
        if actor_genre[i][j] not in actor_genree:
            actor_genree.append(actor_genre[i][j])
        j = j + 1
    actor_genreee.append(actor_genree)
    i = i + 1
#print(actor_genreee)
#----------計算每位演員的類型總和
len_actor_genre = []
i = 0
while i < len(actor_genreee):
    len_actor_genre.append(len(actor_genreee[i]))
    i = i + 1
#print(len_actor_genre)
a_g = dict(zip(nnew_actorr,len_actor_genre))
#print(a_g)
#print(sorted(a_g.items(),key=lambda item:item[1],reverse=True))
print("Top-2 actors playing in the most genres of movies is Brad Pitt, Hugh Jackman, "
      "Scarlett Johansson, Amy Adams, Chloe Grace Moretz, Johnny Depp")
print()
#-------------------------------------------------------------------------------------------------
i = 1
year = []
while i < len(data):
    year.append((data[i][5]))
    i = i + 1
#print(year)
#存每一位演員演出的每個電影年份
actor_year = []
k = 0
while k < len(nnew_actorr):
    i = 0
    aactor_year = []
    while i < len(new_actorr):
        j = 0
        while j < len(new_actorr[i]):
            if new_actorr[i][j] == nnew_actorr[k]:
                aactor_year.append(year[i])
            j = j + 1
        i = i + 1
    actor_year.append(aactor_year)
    k = k + 1
#print(actor_year)
#排序年份
i = 0
actor_year_gap = []
while i < len(actor_year):
    actor_year[i] = sorted(actor_year[i])
    actor_year_gap.append(int(actor_year[i][-1])-int(actor_year[i][0]))
    i = i + 1
#print(actor_year_gap)
#print(nnew_actorr)
a_y_g = dict(zip(nnew_actorr,actor_year_gap))
#print(a_y_g)
#print(sorted(a_y_g.items(),key=lambda item:item[1],reverse=True))
print("Top-3 actors whose movies lead to the largest maximum gap of years is Christian Bale, "
      "Anne Hathaway, Hugh Jackman, Scarlett Johansson, Matt Damon, Mark Wahlberg, Brad Pitt"
      "Christopher Plummer, Tom Hanks, Bryce Dallas Howard, Chiwetel Ejiofor, Ben Kingsley"
      "Gerard Butler, Eva Green, Judi Dench, Will Smith, Jennifer Connelly, Tom Cruise, Emily Blunt"
      "Kevin Spacey, Samuel L. Jackson, Steve Carell, Edward Norton, Will Ferrell, "
      "Denzel Washington, Russell Crowe, Toni Collette, Meryl Streep, Morgan Freeman,"
      "Dominic West, Owen Wilson, Michelle Monaghan, Jessica Biel, Dustin Hoffman, Ben Whishaw,"
      "Paula Patton, Abbie Cornish, Johnny Depp, Jack Davenport, Rachel Weisz, Ellen Burstyn,"
      "Kang-ho Song, Jeremy Irons, Marion Cotillard, Kirsten Dunst, Jennifer Aniston, Justin Theroux,"
      "Maya Rudolph, Kate Bosworth, Audrey Tautou, Luke Wilson, Sacha Baron Cohen, Bob Balaban")
print()
#---------------------------------------------------------------------------------------------------
#存與Johnny Depp合作過的演員
co = []
i = 0
while i < len(new_actorr):
    j = 0
    while j < len(new_actorr[i]):
        if new_actorr[i][j] == "Johnny Depp":
            l = 0
            while l < len(new_actorr[i]):
                if new_actorr[i][l] not in co:
                    co.append(new_actorr[i][l])
                l = l + 1
        j = j + 1
    i = i + 1
#print(co)
#存與co 列表裡合作過的演員
k = 0
colla = co[:]
stop = False
while stop == False:
    while k < len(co):
        i = 0
        while i < len(new_actorr):
            if co[k] in new_actorr[i]:
                j = 0
                while j < len(new_actorr[i]):
                    if new_actorr[i][j] not in co:
                        co.append(new_actorr[i][j])
                    j = j + 1
            i = i + 1
        k = k + 1
    if len(co) == len(colla):
        stop = True
    else:
        colla = co[:]
co = co[1:] #清除掉Johnny Depp
print("all actors who collaborate with Johnny Depp in direct and indirect ways are ",",".join(i for i in co))