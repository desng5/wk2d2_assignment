# Create a function that takes in a integer value 
# representing the a number of seconds
# and returns the seconds converted to hours minutes and seconds
# the output needs to be a string in following format:
# 1H 34M 12S
# 0H 0M 30S
# 24H 12M 0S
# Be sure to use Capital letters to represent H M S

#Jurgita
# def solution(seconds):
#     seconds = seconds % 60
#     minutes = seconds // 60
#     hours = minutes // 60
#     minutes = minutes % 60
#     return f"{hours}H {minutes}M {seconds}S"




#Brians Solution - slower time & space complexity
# def solution(seconds):
#     hours = 0
#     while seconds >= 3600:
#         hours += 1
#         seconds -= 3600
#     minutes = 0
#     while seconds >= 60:
#         minutes += 1
#         seconds -= 60
#     return f"{hours}H {minutes}M {seconds}S"



