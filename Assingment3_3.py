score = input("Enter Score: ")
try:
    s = float (score) #indention error
except:
    print("The input value is wrong")
    quit()
if s>= 0.9:
    print('A')
elif s>= 0.8:  #elif mistake
    print('B')
elif s>= 0.7:
    print("C")
elif s>= 0.6:
    print ('D')
elif s< 0.6 :
    print('F')
