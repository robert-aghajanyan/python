# keep_playing = True
# started = False
# while keep_playing:
#     user_input = input(">").lower()        
#     if user_input == "help":
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
#               ''')
#     elif user_input == "start":
#         if started:
#             print("Car has already started")
#         else:
#             started = True
#             print("Car started... Ready to go!")
#     elif user_input == "stop":
#         if not started:
#             print("Car has already stopped")
#         else:
#             started = False
#             print("Car stopped.")
#     elif user_input == "quit":
#         keep_playing = False
#     else:
#         print("I don't understand that")
   

# numbers = [5, 2, 5, 2, 2]
# for num in numbers:
#     i = 0
#     while i < num:
#         i+=1
#         print('x', end="")
#     print()
       

# numbers = [5,7,8,1,2,9,14]
# max = numbers[0]
# for num in numbers:
#     if num > max:
#         max=num
# print(max)

numbers = [5,6,9,5,8,4,2,3]
new_list = []
for num in numbers:
    if num not in new_list:
        new_list.append(num)
print(new_list)
