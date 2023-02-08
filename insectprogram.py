import insectclass as X

def main(): 
    

    insect1 = X.Insect()
    insect1.flylength()
    

    print(f'The insect can fly:', insect1.get_flight(), 'miles')

main()