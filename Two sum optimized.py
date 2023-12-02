# Two Sum optimized version - Sam Smith, chiefguy.itch.io
nums = []; x = 0; y = (len(nums) - 1); output = []
# user input
print("Welcome to Sum-adder. Made for Leetcode challenge named \"Two Sum\"."); print("Please define target sum to look for and number list."); print()
target = int(input("Target to look for:"))
while True:
     print("Number list:"); print("DOES NOT WORK WITH DUPLICATE NUMBERS."); print(" Your current list is:", nums); print("Do you want to add more to your list?"); print(); print("Type \"y\" for yes, \"n\" for no.")
     temp = input().strip().lower()
     if temp == "y":
          temp = int(input("New number for list:"))
          nums.append(temp)
          continue
     else:
          break
for i in nums:
    if i > target:
        nums.pop(i)
print("Orginal list:", nums, "target:", target)
while x < (len(nums) - 1):
    if y == x:
            print("Error")
            x += 1
            y = (len(nums) - 1)
            continue
    if nums[x] + nums[y] == target:
        output.append(x)
        if y is int(-1):
             y = (len(nums) - 1)
             print("Y:", y)
        output.append(y)
        print("Output:", output)
        break
    else:
        if y > x:
            y -= 1
            continue
        else:
            print("Error")
            x += 1
            y = (len(nums) - 1)
            print("X:", x, "Y:", y)
            continue