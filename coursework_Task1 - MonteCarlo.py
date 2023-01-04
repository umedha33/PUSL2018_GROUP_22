import sys
import random

n = int(sys.argv[1])
# n is the number of repetitions and it is taken from user

def question_1(n):
    
    between_30_35 = 0
    between_36_38 = 0
    between_39_42 = 0

    for i in range (0,n):
        # task a can be completed within 8 - 12 days
        task_a = random.randint(8,12)
        # task b can be completed within 10 - 14 days
        task_b = random.randint(10,14)
        # task b can be completed within 12 - 16 days
        task_c = random.randint(12,16)

        # total days for all tasks = a + b + c
        total_days = task_a + task_b + task_c

        if (total_days > 38) :
            between_39_42+=1
        elif (total_days > 35) :
            between_36_38+=1
        elif (total_days > 29) :
            between_30_35+=1
    
    # this will return probability of each time period so we can get the percentage by *100
    return between_30_35/n, between_36_38/n , between_39_42/n

#this will get returning values and assign them into below variables
[between_30_35, between_36_38, between_39_42] = question_1(500)

# we can get the percentage by *100
print("Likelihood of Completion between_30_35 days : {} %".format(between_30_35*100))
print("Likelihood of Completion between_36_38 days : {} %".format(between_36_38*100))
print("Likelihood of Completion between_39_42 days : {} %".format(between_39_42*100))

