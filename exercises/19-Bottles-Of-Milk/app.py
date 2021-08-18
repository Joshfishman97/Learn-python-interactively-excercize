 def number_of_bottles():
    for a in range(0,100):

         if(i==98):
             return 99+"bottles of milk on the wall, "+i +" bottles of milk."+ 
            "Take one down and pass it around, "+i+" bottles of milk on the wall."
        elif(i!=0):
            return i+"bottles of milk on the wall,"+ i +" bottles of milk. "+"Take one down and pass it around, " + i + " bottles of milk on the wall."
        elif(i==1):
           return'1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.'
        elif(i==0):
           return'No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall. Go to the store and buy some more, 99 bottles of milk on the wall.'
        
    
    number_of_bottles()