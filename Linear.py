
#In the above code, we have created a function linear_Search(), which takes
#three arguments - list1, length of the list, and number to search. We defined
#for loop and iterate each element and compare to the key value. If element
#is found, return the index else return -1 which means element is not present
#in the list.

def linear_Search(list1, key):  
      
        # Searching list1 sequentially  
        for i in range(0, len(list1)):  
            if (list1[i] == key): 
                print(f"Element  {key} found at index: ",  i) 
                return  i
        print("Element not found")
        return None
      
      
list1 = [1 ,3, 5, 4,6, 7, 9]  
key = 9
    
linear_Search(list1, key)  
