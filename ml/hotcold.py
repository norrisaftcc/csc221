# hot and cold learning
# ch4 of grokking deep learning MEAPv8, andrew trask

weight = 0.5
input = 0.5
goal_prediction = 0.8

NUM_ITERATIONS = 1101 # pick amount empirically
step_amount = 0.001 # amount to move our weights each iteration

for iteration in range(NUM_ITERATIONS):
	prediction = input * weight
	# why square the error? for one reason,
	# it must be positive. also amplifies large
	# errors and shrinks small ones
	error = (prediction - goal_prediction) ** 2
	
	print ("Error:", error, "Prediction:", prediction)

	# consider both possibilities --
	# down, or up
	up_prediction = input * (weight + step_amount)
	up_error = (goal_prediction - up_prediction) ** 2

	down_prediction = input * (weight - step_amount)
	down_error = (goal_prediction - down_prediction) ** 2
	
	# use the option with lower error
	if (down_error < up_error):
		weight = weight - step_amount

	if (down_error > up_error):
		weight = weight + step_amount
print("Finished",NUM_ITERATIONS,"runs.")
