import math

def paint(length,width,cover):
    area = length*width
    tins = math.ceil(area/funika)
    print(f"You will need  {tins} tins to paint the house.")
    print("Thank you for trusting us!!")

print("\tWelcome to cover your house\n")
print("Kindly enter the measurements of each: \n")

urefu = int(input("Length: "))
upana = int(input(("Width: ")))
funika = 7
paint(length=urefu,width=upana,cover=funika)