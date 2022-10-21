import random

question_count = 20
question_digits = 2
Questions = list()
question_values = list()
ques_tup = list()

if question_digits < 2 :
    question_digits = question_count

while question_digits>0:
    DoubleDigit = 1
    while DoubleDigit:
        val1 = random.randint(0,9)
        val2 = random.randint(0,9)
        ans = val1 + val2
        #print (a,'+',b, '=', c)
        if 0<ans<10:
            Question = str(val1)+' + ' +str(val2) +' = '+ str(ans)
            tup = sorted((val1, val2))
            if tup in ques_tup:
                x=1
                print(tup, "errrrorororo")
            else:
                DoubleDigit = 0
                print (Question)
                Questions.append(Question)
                ques_tup.append(tup)
                a=ans
                #b,c,d = -1,-1,-1
                #while b < 1 and c < 1 and d < 1 :
                b=ans+random.randint(1,3)
                c=ans-random.randint(1,3)
                d=ans+random.randint(1,3)
                # if ans==0:  #avoiding loop if ans is 0
                #     c=ans+random.randint(1,3)
                # else:
                while c<0:  #avoiding negetive options
                    c=ans-random.randint(1,3)
                    while d == a or d == b or d == c:
                        d=ans+random.randint(0,3)
                options = [a, b, c ,d]
                if question_digits>1:
                    random.shuffle(options)
                question_elements = ((val1, val2, ans, b, c ,d))
                question_values.append(question_elements)
                print (options)
                #print ('a:',a,',b:',b,',c:',c,',d:',d )
                question_digits-= 1

val11=str(question_values[0][0])+str(question_values[1][0])
val22=str(question_values[0][1])+str(question_values[1][1])
anss=str(question_values[0][2])+str(question_values[1][2])
bb=str(question_values[0][3])+str(question_values[1][3])
cc=str(question_values[0][4])+str(question_values[1][4])
dd=str(question_values[0][5])+str(question_values[1][5])

print (val11,'+',val22,'=',anss)
print (anss,',',bb,',',cc,',',dd)