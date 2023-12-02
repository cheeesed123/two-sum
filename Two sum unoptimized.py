# Two Sum unoptimized version - Sam Smith, chiefguy.itch.io

# variables
nums = []
x = 0
y = (len(nums) - 1)
output = []
# user input
print("Welcome to Sum-adder. Made for Leetcode challenge named \"Two Sum\".")
print("Please define target sum to look for and number list."); print()

target = int(input("Target to look for:"))
# list
while True:
     print("Number list:")
     print("DOES NOT WORK WITH DUPLICATE NUMBERS.")
     print(" Your current list is:", nums)
     print("Do you want to add more to your list?"); print()
     print("Type \"y\" for yes, \"n\" for no.")
     
     temp = input().strip().lower()
     # checking input
     if temp == "y":
          temp = int(input("New number for list:"))
          nums.append(temp)
          continue
     else:
          break

# printing it out
print("Orginal list:", nums, "target:", target)
while x < (len(nums) - 1):
    # variables shouldn't match
    if y == x:
            print("Error")
            x += 1
            y = (len(nums) - 1)
            continue
    # checking if matches target.
    if nums[x] + nums[y] == target:
        output.append(x)
        # y shouldn't be -1
        if y is int(-1):
             y = (len(nums) - 1)
             print("Y:", y)
        output.append(y)
        print("Output:", output)
        break
    else:
        # y shouldn't me less than x.
        if y > x:
            y -= 1
            continue
        else:
            print("Error")
            # next x
            x += 1
            y = (len(nums) - 1)
            print("X:", x, "Y:", y)
            continue