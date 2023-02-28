"""
Noah Schwartz

CS 021
"""

def next_collatz(n):

    if n % 2 == 0:
         n = n // 2
         return n
    
    elif n % 2 == 1:
         n = n * 3 + 1
         return n

def collatz(int_input):
     collatz_num = 1
     collatz_new = int_input
     collatz_lst = [int_input]

     while collatz_new > 1:
         collatz_new = next_collatz(collatz_new)
         collatz_lst.append(collatz_new)
         collatz_num = collatz_num + 1


     print(collatz_lst)
     print(f"The length of the sequence is {collatz_num}.")


if __name__ == "__main__":
    int_input = 0
    while int_input < 1:
        int_input = int(input("Enter an integer greater than 1: "))
    print(int_input)
    collatz(int_input)
