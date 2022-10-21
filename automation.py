import random

question_count = 10
question_digits = 5
Questions = list()
question_values = list()
ques_tup = list()


while question_count>0:    
    while question_digits>0:
        DoubleDigit = 1
        while DoubleDigit:
            val1 = random.randint(0,9)
            val2 = random.randint(0,9)
            ans = val1 + val2
            if 0<ans<10:
                Question = str(val1)+' + ' +str(val2) +' = '+ str(ans)
                tup = sorted((val1, val2))
                if tup in ques_tup:
                    x=1
                    print(tup, "errrrorororo")
                else:
                    DoubleDigit = 0
                    Questions.append(Question)
                    ques_tup.append(tup)
                    a=ans                   
                    question_elements = ((val1, val2, ans))
                    question_values.append(question_elements)
                    question_digits-= 1
    question_digits=len(question_values)
    #print (len(question_values))
    val11 = ""
    val22 = ""
    anss = ""
    bb = ""
    cc = ""
    dd = ""
    while question_digits:
        val11 += str(question_values[question_digits-1][0])
        val22=val22+str(question_values[question_digits-1][1])
        anss=anss+str(question_values[question_digits-1][2])
        question_digits-= 1
    answer=int(anss)
    bb=answer+random.randint(1,3*len(question_values))
    cc=answer-random.randint(1,3*len(question_values))
    dd=answer+random.randint(1,3*len(question_values))
    while cc<0:  #avoiding negetive options
        cc=answer-random.randint(1,3)
        while dd == answer or dd == bb or dd == cc:
            dd=answer+random.randint(0,3)
    options = [answer, bb, cc ,dd]
    random.shuffle(options)
    print (val11,'+',val22,'=',answer)
    print (options)
    question_digits=len(question_values)
    question_values=[]
    ques_tup=[]
    question_count-= 1