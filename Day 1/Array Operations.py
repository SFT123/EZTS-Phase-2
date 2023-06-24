#Get one Dynamic array for the given size and perform all operations of DS-insert, delete, search, sort
arr = []
n = int(input("Enter no of Inputs"))
if n<=0:
    print("Invalid Input")
else:
    for i in range(0,n):
            m = int(input("Inputs"))
            arr.append(m)
    inp = int(input("1. Insert \n2.Delete\n3.Search\n4.Sort\n5.Traverse\n6.Exit\nEnter your Choice: "))
    match inp:
        case 1:
            #n = int(input("Enter no of Inputs"))
            #for i in range(0,n):
            m = int(input("Input"))
            arr.append(m)
            print(arr)
        case 2:
            d = int(input("Enter index value to be deleted"))
            del arr[d]
            print(arr)
        case 3:
            s = int(input("Enter Element to Be searched"))
            if s in arr:
                print("Element found at position")
            else:
                print("Element not Found")
        case 4:
            print(sorted(arr))
        case 5:
            print(arr)
        case 6:
            exit