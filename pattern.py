# (star pattern)
# Pattern 1

# row = int(input("Enter the number of rows:"))
# for i in range(0,row):
#     print(" *"*(i+1), end=" ")
#     print()
    
# output:
#          * 
#          * *
#          * * *
#          * * * *
#          * * * * *

# Pattern 2

# row = int(input("Enter the number of rows:"))
# for i in range(0,row):
#     print("  "*(row-i-1), " *"*(i+1), end=" ")
#     print()
#     output:
#                      *
#                    * *
#                  * * *
#                * * * *
#              * * * * *

# Pattern 3

# row = int(input("Enter the number of rows:"))
# for i in range(0,row):
#     print("  "*(i+1), " *"*(row-i), end=" ")
#     print()
#     output:
    #           * * * * * 
    #             * * * * 
    #               * * * 
    #                 * * 
    #                   * 

# Pattern 4

# row = int(input("Enter the number of rows:"))
# for i in range(0,row):
#     print("* "*(row-i), end=" ")
#     print()
#     output:
#              * * * * *  
#              * * * *  
#              * * *  
#              * *  
#              *  

# Pattern 5 
# row = int(input("Enter the number of rows:"))
# for i in range(0,row):
#     print(" "*(row-i-1), "*"*(2*i+1))
    # output:
 #                     *
 #                    ***
 #                   *****
 #                  *******
 #                 *********     
# Pattern 6

# row = int(input("Enter the number of rows:"))
# for i in range(0,row):
#     print(" "*(row-i-1), "* "*(i+1), end=" ")
#     print()
#     output:
#                  *  
#                 * *  
#                * * *  
#               * * * *  
#              * * * * *  

# (number pattern)
# Pattern 6
row = int(input("Enter the number of rows:"))
for i in range(0,row):
    for j in range(0,i+1):
        print(j+1, end=" ")
    print()