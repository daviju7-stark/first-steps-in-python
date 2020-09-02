name1 = input("A name: ")
name2 = input("Other name: ")
final_index_name1=len(name1)-1
final_index_name2 = len(name2)-1

if name1[0] == name2[0] or name1[final_index_name1] == name2[final_index_name2]:
    print("Coincidance")
else:
    print("No coincidance")

