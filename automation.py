import random

QuestionCount = 10
Questions = list()
ques_tup = list()
while QuestionCount>0:
    DoubleDigit = 1
    while DoubleDigit:
        val1 = random.randint(0,9)
        val2 = random.randint(0,9)
        ans = val1 + val2
        #print (a,'+',b, '=', c)
        if ans<10:
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
                d=ans+random.randint(1,3)
                if ans==0:  #avoiding loop if ans is 0
                    c=ans+random.randint(1,3)
                else:
                    c=ans-random.randint(1,3)
                while c<0:  #avoiding negetive options
                    c=ans-random.randint(1,3)
                    while d == a or d == b or d == c:
                        d=ans+random.randint(0,3)
                options = [a, b, c ,d]
                random.shuffle(options)
                print (options)
                #print ('a:',a,',b:',b,',c:',c,',d:',d )
                QuestionCount-= 1

