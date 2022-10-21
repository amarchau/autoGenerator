import random

question_count = 10
question_digits = 2
enable_carry_over = False
questions = list()
question_values = list()
ques_tup = list()


if enable_carry_over:
    carry_var=20
else:
    carry_var=10

while question_count>0:    
    while question_digits>0:
        DoubleDigit = 1
        while DoubleDigit:
            val1 = random.randint(0,9)
            val2 = random.randint(0,9)
            ans = val1 + val2
            if 0<ans<carry_var:
                tup = sorted((val1, val2))
                if tup in ques_tup:
                    x=1
                    print(tup, "errrrorororo")
                else:
                    DoubleDigit = 0
                    ques_tup.append(tup)
                    a=ans                   
                    question_elements = ((val1, val2, ans))
                    question_values.append(question_elements)
                    question_digits-= 1
    question_digits=len(question_values)
    #print (len(question_values))
    value1 = ""
    value2 = ""
    anss = ""
    option_bb = ""
    option_cc = ""
    option_dd = ""
    while question_digits:
        value1 += str(question_values[question_digits-1][0])
        value2=value2+str(question_values[question_digits-1][1])
        anss=anss+str(question_values[question_digits-1][2])
        question_digits-= 1
    #answer=int(anss)
    answer=int(value1)+int(value2)
    option_bb=answer+random.randint(1,3*len(question_values))
    option_cc=answer-random.randint(1,3*len(question_values))
    option_dd=answer+random.randint(1,3*len(question_values))
    while option_cc<0:  #avoiding negetive options
        option_cc=answer-random.randint(1,3)
        while option_dd == answer or option_dd == option_bb or option_dd == option_cc:
            option_dd=answer+random.randint(0,3)
    options = [answer, option_bb, option_cc ,option_dd]
    random.shuffle(options)
    print (value1,'+',value2,'=',answer)
    print (options)
    questions.append(str(value1)+'+'+str(value2)+'='+str(answer))
    questions.append(options)
    question_digits=len(question_values)
    question_values=[]
    ques_tup=[]
    question_count-= 1
print (questions)