def give_change(value):
    hundred_bills = value // 100
    fifty_bills = (value % 100 ) // 50
    rest1 =(value % 100) % 50 
    twenty_bills = rest1 // 20
    rest2 = (rest1 % 50 ) % 20
    ten_bills = rest2 // 10
    rest3 = rest2 % 10
    five_bills = rest3 //5
    rest4 = rest3 % 5
    one_bills = rest4 
    
    
    tuple = (one_bills, five_bills, ten_bills, twenty_bills, fifty_bills, hundred_bills)
    return tuple




