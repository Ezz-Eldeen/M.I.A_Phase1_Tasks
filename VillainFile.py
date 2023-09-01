
import time
def dmg(obj, dmg):  #Polymorphism?
    dmgDone =(dmg-dmg *obj.Shield)
    obj.Health -= dmgDone
    obj.Shield = 0
    print("You've just dealt ",dmgDone, "Damage")
    time.sleep(1)

def validate_input(prompt):     #makes sure the program doesn't throw an error if it got bad input
    while True:
        user_input = input(prompt)
        if user_input.strip():  # Check if the input is not empty after stripping whitespace
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a valid number.")
        
class Villain():
    def __init__(self, name="",Health=100, Energy=500):
        self.name = name
        self.Health = Health
        self.Energy = Energy
        self.Shield = 0
        # print("Constructor invoked")
        

    def Gru(): #gru's turn
        
        stance = validate_input("Choose 1 for Weapons | 2 for Shields: ")
        if stance == 1:
            Weapons.GruWeapons()
        elif stance == 2:
            Shields.GruShields()
        else:
            print("Please choose either 1 or 2")
            time.sleep(1)
            Villain.Gru()
    def Vector(): #Vector's turn
        stance = validate_input("Choose 1 for Weapons | 2 for Shields: ")
        if stance == 1:
            Weapons.vectorWeapons()
        elif stance == 2: 
            Shields.vectorShields()        
class Gadgets():
    def __init__(self,name):
        self.name = name
        self.ecost = 0
        self.resources = 0
        self.desc = ""
    @property   #@property is the decorator that allows us to create a getter for the attribute
    def name(self):
        return self._name

    @name.setter  #setter function
    def name(self, value):
        self._name = value

    @property
    def ecost(self):
        return self._ecost

    @ecost.setter
    def ecost(self, value):
        self._ecost = value

    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        self._resources = value

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value

#inheriting the class since they both shields and weapons share multiple attributes
class Shields(Gadgets):
    def __init__(self, name):
        super().__init__(name)  # calling the parent's constructor to assign the common attributes
        self.shield = 0
        
    
    def GruShields():
        
        print("1.EPBG")
        print("2.Selective Permeability")

        shield = validate_input("Choose your shield of choice: ")      
        if shield == 1:
                
                print("You've put on your ",gs1.shield*100," percent absorption shield")
                gru.Shield = gs1.shield
                gru.Energy -= gs1.ecost
                time.sleep(1)

        elif shield == 2:
            if gs2.resources > 0:
                gs2.resources -=1
                gru.Energy -= gs2.ecost
                print("You've put on your ",gs2.shield*100," percent absorbtion shield")
                print("You now have ",vs2.resources," of this shield left " )
                gru.Shield = gs2.shield
                time.sleep(1)
            else:
                print("You've ran out of this resource.")
                time.sleep(1)
                Shields.GruShields()        
        else:
            print("Please select from the numbers displayed") 
            time.sleep(1)
            Shields.GruShields()     
    def vectorShields():
      
        print("1.Energy Trap Net")
        print("2.Quantum Defelector")

        shield = validate_input("Choose your shield of choice: ")       
        if shield == 1:
            
                print("You've put on your 32 percent absorption shield")
                vector.Shield = vs1.shield
                vector.Energy -= vs1.ecost
                time.sleep(1)
        elif shield == 2:
            if vs2.resources >0:
                print("You've put on your 80 percent absorbtion shield")
                vector.Shield = vs2.shield
                vs2.resources -= 1
                vector.Energy -= vw2.ecost
                print("You now have ",vs2.resources," of this shield left " )
                time.sleep(1)
            else:
                print("You've ran out of this resource.")
                time.sleep(1)
                Shields.vectorShields()       
        else:
            print("Please select from the numbers displayed") 
            time.sleep(1)
            Shields.vectorShields()
class Weapons(Gadgets):
    def __init__(self, name):  
        super().__init__(name) # calling the parent's constructor to assign the common attributes   
        self._dmg = 0 #one underscore for protected, 2 underscores for private

    @property
    def dmg(self):
        return self._dmg

    @dmg.setter
    def dmg(self, value):
        self._dmg = value
        
       
    def GruWeapons():
   
        print("1.", gw1.name)
        print("2.", gw2.name)
        print("3.", gw3.name)
        print("4.", gw4.name)

        weapon = validate_input("Choose your Weapon of Choice: ")

        if weapon == 1:
            
                dmg(vector,gw1.dmg)
                gru.Energy -= gw1.ecost
                # vector.Health -= self.gw1.dmg
                

            
        elif weapon == 2:
            if gw2.resources >0:
                dmg(vector,gw2.dmg)
                gw2.resources -=1
                gru.Energy -= gw2.ecost

            else:
                print("You've ran out of this resource.")
                time.sleep(1)
                Weapons.GruWeapons()    
        elif weapon == 3:
            if gw3.resources >0:
                dmg(vector,gw3.dmg)
                gw3.resources -=1
                gru.Energy -= gw3.ecost
                gru.Shield = 0.2
              
            else:
                print("You've ran out of this resource.")
                time.sleep(1)
                Weapons.GruWeapons()    
        elif weapon == 4:
            if gw4.resources >0:
                vector.Health -= gw4.dmg
                gw4.resources -=1
                gru.Energy -= gw4.ecost
                print("You've just dealt ",gw4.dmg, "Damage")
                time.sleep(1)

            else:
                print("You've ran out of this resource.")
                time.sleep(1)
                Weapons.GruWeapons()          
        else:
            print("Please select from the numbers displayed")
            time.sleep(1)
            Weapons.GruWeapons()
    def vectorWeapons():
        print("1.", vw1.name)
        print("2.", vw2.name)
        print("3.", vw3.name)

        weapon = validate_input("Choose your Weapon of Choice: ")

        if weapon == 1:
           
                dmg(gru,vw1.dmg)                
                
                vector.Energy -= vw1.ecost
                print("You now have ",vw1.resources,"of this weapon left " )
                # vector.Health -= self.gw1.dmg          
        elif weapon == 2:
            if vw2.resources >0:
                dmg(gru,vw2.dmg)
                vw2.resources -=1 
                vector.Energy -= vw2.ecost
                print("You now have ",vw2.resources,"of this weapon left " )
            else:
                print("You've ran out of this resource.")  
                time.sleep(1)
                Weapons.vectorWeapons()  
        elif weapon == 3:
            if vw3.resources >0:
                dmg(gru,vw3.dmg)
                vw3.resources -=1 
                vector.Energy -= vw3.ecost
                print("You now have ",vw2.resources,"of this weapon left " )
            else:
                print("You've ran out of this resource.")  
                time.sleep(1)
                Weapons.vectorWeapons() 
        else:
            print("Please select from the numbers displayed")
            time.sleep(1)
            Weapons.vectorWeapons() 
          
   

gru = Villain("Gru")
vector = Villain("Vector")
#Defining Equipment 
#region
# gw = Gru Weapon
gw1 = Weapons("Freeze gun")
gw1.ecost = 50
gw1.dmg = 11
gw1.resources = "Inf"
gw1.desc = "Minions occasionally wield freeze ray guns that shoot a freezing beam to immobilize opponents temporarily."
gw2 = Weapons("Electric Prod")
gw2.ecost = 88
gw2.dmg = 18
gw2.resources = 5
gw2.desc= "Minions might use electric prods to deliver mild shocks to enemies,stunning them momentarily."
gw3= Weapons("Mega Magent")
gw3.ecost = 92
gw3.dmg = 10
gw3.resources = 3
gw3.desc = " Minions utilize a mega magnet to attract or repel metal objects, potentially disrupting enemy vehicles or equipment."
gw4 = Weapons("Kalman Missile")
gw4.ecost = 120
gw4.dmg = 20 
gw4.resources = 1
gw4.desc = "This unavoidable Missile was created for enourmous distraction"
# gs = Gru Shield
gs1 = Shields("EPBG")
gs1.ecost = 20
gs1.shield = 0.4
gs1.resources = "Inf"
gs1.desc = "The spaceship's shields create an invisible, energy-projected barrier around the vehicle. This barrier absorbs and dissipates energy-based attacks such as lasers, beams, and plasma shots."
gs2 = Shields("Selective Premeability")
gs2.ecost = 50
gs2.shield = 0.9
gs2.resources = 2
gs2.desc = " The shields can be programmed to allow certain objects, signals, or energies to pass through while blocking others. This can be useful for communication or specific tactical maneuvers."


#vw = Vector Weapon
vw1= Weapons("Laser Blasters")
vw1.ecost = 40
vw1.dmg = 8
vw1.resources = "Inf"
vw1.desc = "Vector's primary weapon would be powerful laser blasters attached to his flying pod. These blasters emit focused energy beams that can slice through obstacles and damage enemy vehicles."
vw2 = Weapons ("Plasma Grenades")
vw2.ecost = 56
vw2.dmg = 13
vw2.resources = 8
vw2.desc = "Vector could use plasma grenades that explode on impact, releasing fiery energy bursts that deal significant damage to enemy vehicles caught in the blast radius."
vw3 =Weapons("Sonic Resonance Cannon")
vw3.ecost = 100
vw3.dmg = 22
vw3.resources = 3 
vw3.desc = "Fires powerful sonic waves that can shatter enemy shields and disrupt their systems, temporarily incapacitating them."

#vs = Vector Shield

vs1= Shields("Energy Net Trap")
vs1.ecost = 15
vs1.shield = 0.32
vs1.resources = -1
vs1.desc = "Vector's pod might have the ability to deploy an energy net that ensnares enemy vehicles, temporarily immobilizing them and leaving them vulnerable to Vector's other attacks."
vs2 = Shields("Quantum Deflector")
vs2.ecost = 40 
vs2.shield = 0.8
vs2.resources = 3
vs2.desc = "Manipulates quantum states to create a deflection field, causing enemy projectiles to miss the spaceship by a slight margin in the quantum realm."

#endregion
