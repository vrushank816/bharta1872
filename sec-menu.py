import math
menu = {
'burger' : 50,
'pizza': 160,
 'puff': 30,
 'vadapav': 35,
  'fries': 40
}
setting =['1. Add New Item', '2. Change Price']

def set_1(): #add new item
	add=input('new Food - ')
	n_price=int(input("new price - "))
	menu[add]= n_price
	print('-------------------')
	for item in menu:
		print(item ,menu[item])
	print('-------------------')

def set_2():
	N_name = (input("Name of Food - "))
	if N_name in menu:
		N_price = int(input("New Price - "))
		menu[N_name]= N_price
		print('-------------------')
		for item in menu:
			print(item ,menu[item])
		print('-------------------')


print("------- Menu -------")
for item in menu:
	print(item ,menu[item])
print("--------------------")
order ={}

while True:
	choice = input("Enter Your Order Or done to Finish - ")

	if choice in menu:
		qnt = int(input("Enter Quntity - "))
		order[choice]= qnt
	if choice == "done":
		break;
	if choice == "setting":
		for i in setting:
			print(i)
		set_choice=int(input('Select Your changes - '))
		
		if set_choice == 1:
			set_1()		
		
		if set_choice == 2:
			set_2()			
			
				
				
		
Bill =[]
print("\n----- Your Order -----")
for item, qnt in order.items():
    print(item,qnt)
    Bill.append(menu[item]*qnt)

print('\n----Bill-----')

while True== choice:
	print(f'{choice } = {qnt}')
print(math.fsum(Bill))
    
    
