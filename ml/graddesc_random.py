# ch 4 continued
# gradient descent - calculate both direction of error
# and amount of error
# modified to learn a random number between zero and one
import random

weight = 0.5
goal_pred = random.random()
input = 0.5
# note that starting at 0.5 (weight=0.5, input=1.0) 
# gets it in one try, which is less interesting
print ("I will now attempt to guess the number",goal_pred)
for iter in range(20):
	pred = input * weight
	# error is 'pure error'
	error = (pred - goal_pred) ** 2
	# scale by input (this handles the edge cases
	# at which pure error is insufficient --
	# scaling, negative reversal, and stopping
	direction_and_amount = (pred - goal_pred) * input
	weight = weight - direction_and_amount

	print("Error:", error, "Prediction:", pred)
