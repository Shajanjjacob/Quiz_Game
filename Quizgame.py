print("****************************************************")
print(
    '''
 __          __  _                            _______      __  __          ____        _     
 \ \        / / | |                          |__   __|    |  \/  |        / __ \          
  \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___   | \  / |_   _  | |  | |_   _ _ ____
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \  | |\/| | | | | | |  | | | | | |_  /
    \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) | | |  | | |_| | | |__| | |_| | |/ / 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|_   |_|\___/  |_|  |_|\__, |  \___\_\\__,_|_/___|
                                       / ____|                     __/ |                     
                                      | |  __  __ _ _ __ ___   ___|___/                      
                                      | | |_ |/ _` | '_ ` _ \ / _ \                          
                                      | |__| | (_| | | | | | |  __/                          
                                       \_____|\__,_|_| |_| |_|\___|                          
                                                                     '''
)
question_bank=[
    {"text":"The ability of one clas to acquire  the methods  and attributes of another class is called________ ","Answer":"A"},
    {"text":"which of the following is a type of inheritances ________","Answer":"D"},
    {"text":"Which type of inheritances has multiple subclasses to a single superclass?","Answer":"C"},
    {"text":"what is the depth of multilevel inheritances in python?","Answer":"C"},
    {"text":"what does MRO stands for______","Answer":"B"},
]
option=[["A.inheritances","B.Abstration","C.polymorphism","D.object"],
        ["A.single","B.Double","C.multiple","D.Both A and c"],
        ["A.multiple inheritance","multilevel inheritance ","C.Hierarchical inheritance","D.None of these"],
        ["A.Two level","B.Three level","C.Any level","D.None of these"],
        ["A.method rescursive object","B.Method resoluation order","C.main resolution order","D.Method resoluation object"]
        
        ]
score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False
    
for question_num in range (len(question_bank)):
    print("###**************************************###")
    print(question_bank[question_num]['text'])
    for i in option[question_num]:
        print(i)

    guess=input("Enter your choice A/B/C/D:\n").upper()
    is_correct=check_answer(guess,question_bank[question_num]["Answer"])
    if is_correct:#true
        print("correct Answer")
        
        score+= 1
        print(f"{score}/{question_num+1}")
       
    else:
        print("incorrect Answer")
        print(f"The correct  answer is {question_bank[question_num]['Answer']} ")
print(f"The final score is = {score},In percentage={(score/len(question_bank))*100}%")
