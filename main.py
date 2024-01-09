print("   1     2     3")
row1 = ["◻️","◻️","◻️"]
row2 = ["◻️","◻️","◻️"]
row3 = ["◻️","◻️","◻️"]
map = [row1, row2, row3]
print(f"1{row1}\n2{row2}\n3{row3}")
position = input("Where do you want to put the treasure?\nEnter a double digit number, the row, then space. ex.'23': ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = (map[vertical - 1])
selected_row[horizontal - 1] = "X"

print(f"1{row1}\n2{row2}\n3{row3}")