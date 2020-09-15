def linear_search(value,search_for):
       search_at=0
       search_res=false
       while search_at<len(values) and
         search_res is false:
                    if values[search_at]== search_for:
                    search_res=true
                    print('element inthe position',search_at)
                 else:
                        search_at=search_at+1
          return search_res
list=['niki','utsav','tanvi','vedangi','nidhi']
print(linear_search(list,'aman'))
print(linear_search(list,'niki'))
list.reverse()
print("reverse of the number is=",list)
list.sort()
print("sorted list of the number is=",list)
list.sort(reverse=true)
print("the list in descending order is=",list)
