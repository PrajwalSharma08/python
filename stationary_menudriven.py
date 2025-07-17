c="y"
while c=="y" or c=="Y":
    print("what do u want?",'\n','1=pen (5rs/unit)','\n','2=books (150rs/unit)','\n','3=copy(50rs/unit)')
    a=input('enter a item no.')
    if a=='1':
        b=int(input('quantity?'))
        d=b*5
        print('apke itne rupee hue',d)
    elif a=='2':
        b=int(input('quantity?'))
        d=b*150
        print('apke itne rupee hue',d)
    elif a=='3':
        b=int(input('quantity?'))
        d=b*50
        print('apke itne rupee hue',d)
    else:
        print("try again")
    c=input("require something else:(Y/N)")
    if c=='N' or c=='n':
        print('Dhanyawaad apka❤️❤️')
