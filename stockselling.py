
def stockBuySell(price, n):
	
	
	if (n == 1):
		return
	
	
	i = 0
	while (i < (n - 1)):
		
		
		while ((i < (n - 1)) and
				(price[i + 1] <= price[i])):
			i += 1
		
		
		if (i == n - 1):
			break
		
		
		buy = i
		i += 1
		
		
		while ((i < n) and (price[i] >= price[i - 1])):
			i += 1
			
		
		sell = i - 1
		
		print("Suggestion to Buy on day: ",buy,"\t",
				"Suggstion to Sell on day: ",sell)
		

n = int(input("Enter the trading days: "))
print("Input the daily stock price: ")
price = [int(input()) for i in range(n)]


print(stockBuySell(price, n))


