import sys
import random

n = int(sys.argv[1])
# n is the number of repetitions and it is taken from user

def question_2(n):
    #a child can be a girl or a boy, so P(girl) = 1/2
    all_girls = 0; at_least_a_girl = 0

    for i in range (0, n):
        child_1 = random.randint(1,2)
        child_2 = random.randint(1,2)
        child_3 = random.randint(1,2)
        
        # lets take random number 1 as a girl and 2 as a boy

        # if child 1,2 and 3 all are girls this will increment the count of all_girls
        if child_1 == 1 and child_2 == 1 and child_3 == 1:
            all_girls+=1

        # if child 1,2 or 3 is a girl this will increment the count of at_least_a_girl
        if child_1 == 1 or child_2 == 1 or child_3 == 1:
            at_least_a_girl+=1 

    return all_girls, at_least_a_girl
        
#this will get the returning values and assign them to below variables
[all_girls, at_least_a_girl] = question_2(n)

#now we have the ruslts as variables and we can perform any task with them
print("probability of having at least one girl - {}".format(at_least_a_girl/n))
print("probability of having 3 girls - {}".format(all_girls/n))   





