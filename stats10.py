
import random
#Problem 34, parcheesi
#Component: 2 random number 1-6 representing a dice. if numbers sum to 3, or one is 3, end trial. 
#Trial: generate numbers until condition is met, representing end of the game
#Response: Number of rolls needed to end the game
#Statistic: Mean

num_trials = 1000
num_of_rolls = 0

for x in range(num_trials):
	#Trial
	done = False
	while not done:
		num_of_rolls = num_of_rolls + 1
		d1 = random.randint(1,6)
		d2 = random.randint(1,6)
		if d1+d2==3 or d1==3 or d2==3:
			#response
			done = True 

#statistic
print("Average number of rolls needed to end the Parcheesi game 3 spaces away:")
print(num_of_rolls/num_trials)


#Problem 40
#component: a random integer 0-9, representing the chance a person is texting while driving, with 0 representing texting, and 1-9 representing not texting
#trial: 20 random integers respresenting people observed
#response: the percent of trials that have 5 or more people texting (amount of trials with 5 or more 0s)
#statistic: proportion


num_trials = 1000
true_trials = 0
for x in range(num_trials):


    #trial
    total_texter = 0
    for y in range(20):
    	driver = random.randint(0,9)
    	if driver == 0:
    		total_texter = total_texter + 1

    #response
    if total_texter >= 5:
        true_trials = true_trials + 1
#statistic
print("Percent of trials having 5 or more texters:")
print(100*true_trials/num_trials)



#Problem 35
#component: random number 1-100, with 1-65 representing a sucsessful shot, and 66-100 representing a miss
#trial: 20 components representing 20 shots taken
#response: percent of time 6 shots in a row are sucsessful
#statistic: proportion

num_trials = 1000
true_trials = 0
for x in range(num_trials):

        #trial
        shots_in_row = 0
        success = False
        for y in range(20):
                shot = random.randint(1,100)
                if shot <= 65:
                        shots_in_row = shots_in_row + 1
                        if shots_in_row == 6:
                                success = True
                else:
                        shots_in_row = 0

        #response
        if success:
                true_trials = true_trials + 1

print("percent that 6 shots are made in a row in a game")
print(100*true_trials/num_trials)











                        
