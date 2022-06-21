import traceback
def calculator():
    
    # Get dog age
    age = input("Input dog years: ")

    try:
        # Cast to float
        dog_age = float(age)
        human_age = 0

        # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years
        
        # your code here
        if dog_age < 0:
            print('your input: ', age,' is negative,', 'please input a positive number')
        elif dog_age > 0 and dog_age <= 1:
            human_age = 15
            dog_age = dog_age * human_age         
        elif dog_age > 1 and dog_age <= 2:
            human_age = 12
            dog_age = dog_age * human_age
        elif dog_age > 2 and dog_age <= 3:
            human_age = 9.3
            dog_age = dog_age * human_age
        elif dog_age > 3 and dog_age <= 4:
            human_age = 8
            dog_age = dog_age * human_age
        elif dog_age > 4 and dog_age <= 5:
            human_age = 7.2
            dog_age = dog_age * human_age         
        else:
            human_age = 7
            dog_age = dog_age * human_age
           
        dog_age = round(dog_age, 2)  
        
        if dog_age > 0:
            print('The given dog age: ', age, ' is ', dog_age, 'in human years.')
    
    except ValueError as e:
        print(age, 'is an invalid age, please input a numberical digit')
        print(traceback.format_exc())
    
calculator() # This line calls the calculator function