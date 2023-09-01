
from VillainFile import Villain, gru, vector
turns = 0
def Main():
    global turns # So I can use this as a global variable

    if __name__ == "__main__" :
        if gru.Health >0 and vector.Health > 0:

            print("Gru's Stats:    Vector's Stats:")
            print("------------    ---------------")
            print("HP:",gru.Health, "        HP: ", vector.Health)
            print("Energy:", gru.Energy,"    Energy: ",vector.Energy)
            print("Shield:",gru.Shield *100, "%", "      Shield: ",vector.Shield*100,"%")

            if turns%2 == 0 and gru.Health > 0 and vector.Health > 0 :
                print("----------------")
                print("Gru's Turn")
                print("----------------")
                Villain.Gru()
                turns +=1
                print("Turn:", turns)
                Main()

            elif turns%2 == 1 and gru.Health > 0 and vector.Health > 0:
                # vector.Vector()
                print("----------------")
                print("Vector's Turn")
                print("----------------")
                Villain.Vector()
                turns +=1
                                
                Main()
        elif gru.Health >0 and vector.Health <=0:
            print("Vector Has Been Defeated!")
        elif gru.Health <= 0 and vector.Health >0:
            print ("Gru Has Been Defeated!")    
        
Main()