#Use Case: Airline Seat Reservation System

#1. Create Seat Tuple
seats = ("1A", "1B", "1C", "2A", "2B", "2C")
set_seats = set(seats) # Convert to set for uniqueness
seats = tuple(set_seats) # Convert back to tuple
print("Available Seats:", seats)

#2. Access Seat Using Index
print("First Seat:", seats[0]) # 1A
print("Last Seat:", seats[-1]) # 2C

#3. Iterate Through Seats (Loop)
print("All Seats:")
for seat in seats:
    print(seat, end=' ')
    
#4. Count Seat Occurrence (count())
print("\nCount of Seat '1A':", seats.count("1A")) # 1

#5. Find Seat Position (index())
print("Index of Seat '2B':", seats.index("2B")) # 4

#6. Tuple Packing
seat_info = ("A1", "Window", "Economy")
print("Seat Information:", seat_info)

#7. Tuple Unpacking
seat_number, seat_type, seat_class = seat_info
print("Seat Number:", seat_number) # A1
print("Seat Type:", seat_type) # Window
print("Seat Class:", seat_class) # Economy

#8. Combine Tuples
additional_seats = ("3A", "3B", "3C")
all_seats = seats + additional_seats
print("All Available Seats:", all_seats)

#9. Convert Tuple to List for Modification
seat_list = list(seats)
seat_list.append("3D") # Add new seat
seats = tuple(seat_list) # Convert back to tuple
print("Updated Seats:", seats)

#10. Tuple Length
print("Total Seats Available:", len(seats)) # 7





