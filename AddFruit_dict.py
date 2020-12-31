def addfruit(fruit1,price1):
    fruit_dict={}
    i=0
    while i!=len(fruit1):
        try:
            if fruit1[i].lower() not in fruit_dict:
                fruit_dict.update({fruit1[i]:price1[i]})
                i+=1
            else:
                i+=1
                raise ValueError
        except: 
            if ValueError:
                print(f"Error : {fruit1[i]} is allready in dict")
        
    return fruit_dict 