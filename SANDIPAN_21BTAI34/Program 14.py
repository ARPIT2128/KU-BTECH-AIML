def linearSearch(lst,item):
  for i in range(len(lst)):
    if lst[i]==item:
      return f"The element {item} is at index {i}"    
  return -1    
def binarySearch(lst,item):
  lst.sort()
  print("The sorted list is:",lst)
  low,high=0,len(lst)-1
  while low<=high:
    mid=(low+high)//2
    mid_element=lst[mid]
    if mid_element==item:
      return f"The element {item} is at index {mid}"    
    if mid_element<item:
      low=mid+1    #discarding the right part of the list because item is greater than middle element
    elif mid_element>item:
      high=mid-1    #discarding the left part of the list becasue item is smaller then middle element
    return -1
ls=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(n):
  ls.append(int(input()))
print("Your list is: ",ls)
it=int(input("Enter item to search: "))
ch=int(input("Enter 0 for linear search and 1 for binary search: "))
if ch==0:
  print(linearSearch(ls,it))
else:
  print(binarySearch(ls,it))
