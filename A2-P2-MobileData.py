#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #:     
#Student Name:Lucas  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
   
   totaldata=float(input("how much data did you use?")) #getting the user input for data
   
   if totaldata<=200:
    rateofcharge=20
    print(rateofcharge, "here is how much mb of data you used")
    
   elif totaldata >200 and totaldata <500 : #making it so if they type a number between 200 and 500 it will charge them 0.105
     finaltotal=rateofcharge=0.105*totaldata
     print(finaltotal, "here is how much mb of data you used")
     
   elif totaldata>=500 and totaldata <1000:
    finaltotal=rateofcharge=0.110*totaldata 
    print(finaltotal, "here is how much mb of data you used")
    
   elif totaldata>=1000:
    finaltotal=118
    print(finaltotal, "you have used over a GB") #changed the print text if they are over 1000mb
    


    # YOUR CODE ENDS HERE

main()