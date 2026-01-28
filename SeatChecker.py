available_seats=5
while available_seats>0:
    print(f"available seats {available_seats}")
    book=input("want to book seats(yes/no): ").lower()
    if book=="yes":
        available_seats-=1
        print("seats booked")
        
    else:
        print("no seats booked")
       
print("all seats booked") 