import insectclass as X

def main(): 
    

    insect1 = X.Insect('mosquito', 2,4)
    insect1.flylength()
    insect2= X.Insect('housefly',2,4)
    insect2.flylength()
    

    print(f'The {insect1.get_name()} can fly:', insect1.get_flight(), 'miles')
    print(f'The {insect2.get_name()} can fly:', insect2.get_flight(), 'miles')
main()