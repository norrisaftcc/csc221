# ch 4 continued
# gradient descent - calculate both direction of error
# and amount of error

weight = 0.5
goal_pred = 0.8
input = 0.5

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
