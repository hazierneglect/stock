def simple_moving_average(STOCKAdj, startday, length):
	# STOCKAdj	list with all closing values
	# days		number of days (20, 50, 100)
	# startday	the beginning day (right now, numerical)
	
	if startday < length:
		return None
	# stockprices	fetches only the closing values we need, in reverse order
	stockprices = STOCKAdj[startday:(startday-length):-1]
	
	
	stockprices = STOCKAdj[(startday-length):startday]
	stockprices.reverse()

	SMA = sum(float(eachprice) for eachprice in stockprices)/len(stockprices)

	return SMA
	



# input  1,2,3, [], 


def exponential_moving_average(STOCKAdj, startday, length, oldEMA):
	
#EMA: {Close - EMA(previous day)} x multiplier + EMA(previous day). 

	# Multiplier is calculated like this: (2 / (Time periods + 1) ) 
	# EMA,
	# stockprices
	if startday < length:
		return None#float(STOCKAdj[startday]) #float(stockprices[1])
	# stockprices	fetches only the closing values we need, in reverse order
	elif startday == length:
		return simple_moving_average(STOCKAdj, startday, length)
	else:
		stockprices = STOCKAdj[(startday-length):startday]
		stockprices.reverse()
	
		for x in range(0, len(stockprices)):
			stockprices[x]=float(stockprices[x])
		alpha = 2./(length+1)
		
	#	 stockprices, startday
		# float(STOCKAdj[startday]) - oldEMA[len(oldEMA)-1]
		
		## off by one error
	#	EMA = (float(STOCKAdj[startday])-oldEMA[len(oldEMA)-1])*alpha + oldEMA[len(oldEMA)-1]
		EMA = (float(stockprices[0])-oldEMA[len(oldEMA)-1])*alpha + oldEMA[len(oldEMA)-1]
		# Weight input EMA by day, farther back is multiplied by alpha^history
		#EMA PREVIOUS DAY (SUM)

	
		return EMA
	


"""
moving average convergence divergence
KDJ indicator
relative strength index
Williams %R
bias ratio
bollinger bands
fast stochastic oscillator
slow stochastic oscillator
commodity channel index
volume moving average
"""