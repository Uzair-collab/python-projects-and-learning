actual_sale = float (input ("enter the selling price:"))
actual_cost = float (input(" enter the actual price:"))

if (actual_sale > actual_cost):
    profit = actual_sale - actual_cost
    print("profit:", profit)
else:
    loss = actual_cost - actual_sale
    print("loss: ", loss) 




    