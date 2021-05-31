operator = ["+","-","*","^"]
num_string = ["0","1","2","3","4","5","6","7","8","9"]
a = input("input the polynomials: ")
a = a[1:-1]#先移除開頭的"("，以及結尾的")"
k = a.split(")(")
#------------------有'-'在字串裡的時候，在'-'前加上'+'
i = 0
while i < len(k):
    j = 0
    while j < len(k[i]):
        if k[i][j] == '-':
            k[i] = k[i][0:j]+ "+" + k[i][j:]
            j = j + 2                       #如果是 j = j + 1 的時候，依舊會指到新字串的"-"。
        else:
            j = j + 1
    i = i + 1
#print(k)
#----------------在字串的頭加入"+"
i = 0
while i < len(k):
    if k[i][0] != "+":
        k[i] = "+" + k[i]
    i = i + 1
#print(k)
#----------------如果'-'後面不是數字時，在'-'後面補上'1*'
i = 0
while i < len(k):
    j = 0
    while j < len(k[i]):
        if k[i][j] == '-' and k[i][j+1] not in num_string:
            k[i] = k[i][0:j+1] + "1*" + k[i][j+1:]
            j = j + 1
        else:
            j = j + 1
    i = i + 1
#print(k)
#----------------如果'+'的後面不是'-'也不是數字時，在'+'後面補上'1*'
i = 0
while i < len(k):
    j = 0
    while j < len(k[i]):
        if k[i][j] == '+' and k[i][j+1] not in num_string and k[i][j+1] != "-":
            k[i] = k[i][0:j+1] + "1*" + k[i][j+1:]
            j = j + 1
        else:
            j = j + 1
    i = i + 1
#print(k)
#-------------------用"+"來切字串
kk = []
i = 0
while i < len(k):
    kk.append(k[i].split("+"))
    i = i + 1
#print(kk)
#-----------------把第一項去除
i = 0
while i < len(kk):
    kk[i] =  kk[i][1:]
    i = i + 1
#print(kk)
#-----------------用"*"切字串
kkk = []
i = 0
while i < len(kk):
    j = 0
    kkkk = []
    while j < len(kk[i]):
        kkkk.append(kk[i][j].split("*"))
        j = j + 1
    kkk.append(kkkk)
    i = i + 1
#print(kkk)
#------------------------------把次方換成變數，例如x^2y^3，變成xx2yyy3
i = 0
while i < len(kkk):
    j = 0
    while j < len(kkk[i]):
        k = 0
        while k < len(kkk[i][j][1]):
            new_power = ""
            if kkk[i][j][1][k] == "^":
                new_power = (kkk[i][j][1][k-1]) * (int(kkk[i][j][1][k+1])-1)
                #print(new_power)
                kkk[i][j][1] = kkk[i][j][1].replace("^",new_power,1)
            k = k + 1
        j = j + 1
    i = i + 1
#print(kkk)
#----------------------------------把xx2yyy3的數字移除，變成xxyyy
i = 0
while i < len(kkk):
    j = 0
    while j < len(kkk[i]):
        k = 0
        while k < len(kkk[i][j][1]):
            if kkk[i][j][1][k] in num_string:
                kkk[i][j][1] = kkk[i][j][1].replace(kkk[i][j][1][k],"")
                continue
            else:
                k = k + 1
        j = j + 1
    i = i + 1
#print(kkk)
#--------------------------------依照分配律做乘法運算
kkkk = []
kkkk.append(kkk[0])
kkk = kkk[1:]
m = 0
while m < len(kkk):
    kkkk.append(kkk[m])
    c_new = []
    v_new = []
    i = 0
    while i < len(kkkk[0]):
        j = 0
        while j < len(kkkk[1]):
            c_new.append(str((int(kkkk[0][i][0])) * (int(kkkk[1][j][0]))))
            v_new.append(kkkk[0][i][1] + kkkk[1][j][1])
            j = j + 1
        i = i + 1
    #print(kkkk)
    kkkkk = []
    h = 0
    while h < len(c_new):
        kkkkk.append([c_new[h]] + [v_new[h]])
        h = h + 1
    kkkk = []
    kkkk.append(kkkkk)
    #print(kkkk)
    m = m + 1
#print(kkkk)
#print(c_new)
#print(v_new)
#------------------------------------將出現過的變數存入list
variable = []
i = 0
while i < len(v_new):
    j = 0
    while j < len(v_new[i]):
        if v_new[i][j] not in variable:
            variable.append(v_new[i][j])
        j = j + 1
    i = i + 1
#print(variable)
#-------------------------------------將字母按照順序排序
i = 0
while i < len(v_new):
    v_new[i] = sorted(v_new[i])
    v_new[i] = "".join(v_new[i])
    i = i + 1
#print(v_new)
#-----------------------------------將相同指數的多項式係數合併，並移除多的變數項
i = len(v_new) - 1
while i > 0:
    j = i - 1
    while j > 0:
        if v_new[i] == v_new[j]:
            c_new[i] = str((int(c_new[i]))+(int(c_new[j])))
            c_new.remove(c_new[j])
            v_new.remove(v_new[j])
        j = j - 1
    i = i - 1
#print(c_new)
#print(v_new)
#---------------------------------將xxyyy改回x^2y^3
i = 0
ttemp = []
while i < len(v_new):
    k = 0
    count = 0
    temp = ""
    while k < len(variable):
        count = v_new[i].count(variable[k])
        if count == 0:
            pass
        if count == 1:
            temp = temp + variable[k]
        if count > 1:
            temp = temp + variable[k] + "^" + str(count)
        #print(count)
        k = k + 1
    ttemp.append(temp)
    i = i + 1
#print(ttemp)
#-------------------------------如果合併係數後為零，移除該項
i = len(ttemp) - 1
while i > 0:
    if int(c_new[i]) == 0:
        c_new.remove(c_new[i])
        ttemp.remove(ttemp[i])
    i = i - 1
#print(ttemp)
#print(c_new)
#------------------------------如果係數為-1時，在變數前加'-'號，如果係數為1時，變數不做動作。
#------------------------------其他狀況，將係數加'*'加變數
final = []
i = 0
while i < len(ttemp):
    if c_new[i] == "-1":
        final.append("-" + ttemp[i])
    elif c_new[i] == '1':
        final.append(ttemp[i])
    else:
        final.append(c_new[i] + "*" + ttemp[i])
    i = i + 1
#print(final)
#--------------------------------如果開頭是'-'號則直接合併，不是的話在中間加入'+'
ans = final[0]
i = 1
while i < len(final):
    if final[i][0] == "-":
        ans = ans + final[i]
    else:
        ans = ans + "+" + final[i]
    i = i + 1
print("Output result:",ans)