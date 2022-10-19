import random

Questions = list()
QuestionCount = 5
while QuestionCount>0:
    DoubleDigit = 1
    while DoubleDigit:
        val1 = random.randint(0,9)
        val2 = random.randint(0,9)
        ans = val1 + val2
        #print (a,'+',b, '=', c)
        if ans<10:
            Question = str(val1)+' + ' +str(val2) +' = '+ str(ans)
            if Question in Questions:
                x=1
            else:
                DoubleDigit = 0
                print (Question)
                Questions.append(Question)
                a=ans
                b,c,d = -1,-1,-1
                while b < 1 and c < 1 and d < 1 :
                    b=ans+random.randint(0,3)
                    c=ans-random.randint(0,3)
                    d=ans+random.randint(0,3)
                    while d == a or d == b or d == c:
                        d=ans+random.randint(0,3)
                    print ('a:',a,',b:',b,',c:',c,',d:',d )
                    QuestionCount-= 1


                    #hello india