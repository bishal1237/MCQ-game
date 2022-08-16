print("Welcome to quiz game.")


ask = input('Do yo wanna play! ')
ask_accept = ask.lower()


if ask_accept != "yes":
    quit()
else:
    print("Lets Start quiz game")
    
    
score = 0    
    

            # Question 1
    
question = input('Whats the full form of PC ? ')
questionAns = question.lower()

if question.lower() == "personal computer":
    print("Correct!")
    score += 1 
else:
    print('Wrong!')
    


           # Question 2    
question = input('Whats the full form of CPU ? ')
questionAns = question.lower()

if question.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print('Wrong!')
    
    
    
           # Question 3   
question = input('Whats the full form of MCQ ? ')
questionAns = question.lower()

if question.lower() == "multiple choice question":
    print("Correct!")
    score += 1
else:
    print('Wrong!')   
    
    
    
           # Question 4  
question = input('Whats the full form of HTML ? ')
questionAns = question.lower()

if question.lower() == "hypertext markup language":
    print("Correct!")
    score += 1
else:
    print('Wrong!')   
    
    
    
           # Question 5  
question = input('In which year HTML was first proposed ? ')
questionInt = int(question)
if questionInt== 1990:
    print("Correct!")
    score += 1
else:
    print('Wrong!') 
    
    
    
    
               # Question 6 
question = input('Whats the full form of CSS ? ')
questionAns = question.lower()

if question.lower() == "cascading style sheets":
    print("Correct!")
    score += 1
else:
    print('Wrong!')  
    
    
    
                   # Question 7
question = input('Whats the full form of SQL ? ')
questionAns = question.lower()

if question.lower() == "structured query language":
    print("Correct!")
    score += 1
else:
    print('Wrong!')  
     
     
     
                    # Question 8 
question = input('Whats the full form of PHP ? ')
questionAns = question.lower()

if question.lower() == "hypertext preprocessor":
    print("Correct!")
    score += 1
else:
    print('Wrong!')
    
    
    
                   # Question 9  
question = input('Whats the full form of PDF? ')
questionAns = question.lower()

if question.lower() == "portable document format":
    print("Correct!")
    score += 1
else:
    print('Wrong!')

    
    
                   # Question 10 
question = input('Whats the full form of URL ? ')
questionAns = question.lower()

if question.lower() == "uniform resource locator":
    print("Correct!")
    score += 1
else:
    print('Wrong!')
    
    
    
    
    
print(f'You score is {score}/10 .')    
