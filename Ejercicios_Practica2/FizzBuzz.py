# fizz entre 3 buzz entre 5 bizzbuzz entre 3 y 5
# for i in range(1,101): 
#     if i%3 == 0 and i%5!=0 :
#         print("Fizz")
#     elif i%3!=0 and i%5==0:
#         print("Buzz")
#     elif i%3==0 and i%5==0:
#         print("FizzBuzz")
#     else:
#         print(i)
    
def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    if numero % 3 == 0:
        return "Fizz"
    if numero % 5 == 0:
        return "Buzz"
    return(str(numero))