
# Program for printing desired star pattern

print("Enter no. of rows you want a star pattern")
num = input("Enter no. of rows:\n")
print("Enter type of pattern as either str or rev")

pat = input("Enter pattern:\n")

try:
    if pat=="str":
        i1 = 0
        while i1<=int(num):
            print("*"* i1)
            i1+=1
    elif pat=="rev":
        i2 = int(num)
        while i2>0:
            print("*"*i2)
            i2-=1
    else:
        print("Something went wrong!\nTry again.")
except:
    print("Something went wrong!\nTry again.")

# if pat=="str":
#     i1 = 0
#     while i1<=int(num):
#         print("*"* i1)
#         i1+=1
# elif pat=="rev":
#     i2 = int(num)
#     while i2>0:
#         print("*"*i2)
#         i2-=1
# elif (pat=="str" or pat=="rev") and (int(num)!=int):
#     print("Row number should be an integer!\nTry again.")
# elif pat!=("str" or "rev"):
#     print("Something went wrong!\nMay be pattern given by you is invalid!\nTry again.")
# else:
#     print("Something went wrong!\nTry again.")
