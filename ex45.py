import random
from sys import exit
import ex45_fates
import ex45_entry_desc


class Engine(object):
        
    def __init__(self, fates_map):
        #import dict, make usable
        self.fates_map = fates_map
        
    def play(self):
        #use dict to create instance of init_fates_name func.
        current_apt = self.fates_map.init_fates_name() 
        last_apt = self.fates_map.ret_fates_name('lease_signed')
        
        
        while current_apt != last_apt:
	    #Instantiate var fed into __init__ func call it
            #with dict val.
            next_apt_name = current_apt.arrive()
            next_apt_name = current_apt.enter()
          
            current_apt = self.fates_map.ret_fates_name(next_apt_name)   
                                      

class Apartment(object):
    
    def arrive(self):
        #Housing for repetitive option to give up or go on
        print "Do you want to give up or go on to the next?"
        
        answer = raw_input("> ")
        
        if answer == "give up":
            print "Your folks miss you anyway. Bye bye!"
            exit(1)
        elif answer == "go on":
            self.enter()
        elif answer == "next":
            self.enter()
        elif answer == "go on to the next":
            self.enter()

    def enter(self):
        print "This rooms desc."
        exit(1)
        
        
class EvilLandlord(Apartment):

    def arrive(self):
        #Overwrite Supers arrive func then pass over it.
        pass

    def enter(self):
        print ex45_entry_desc.evil_landlord
                 
        question = raw_input("Do you have any questions? > ")
        
        while question != "no":
        
            if "safe" in question:
                print """We haven't had any break-ins here since
                      installing the bars over the back window.
                      """
	    elif "yes" in question:
		print "Great, what would you like to know?"
            elif "dishwasher" in question:
                print """There are so many great restaurants 
                      around here that you'll never be eating
                      at home anyway.
                      """
            elif "washing machine" in question:
                print "There's a laundrymat right around the corner."  
            else:
                print """I don't know, that's a good question. These
                      apartments go so fast I never have time to 
                      get all the details.
                      """ 
            question = raw_input("Any other questions?  >")                                 
                
                           
        lease = raw_input("Great would you like to go ahead and sign your lease? > ")
        
        if lease == "yes":
            print ex45_fates.bad_fate
            exit(1)
        elif lease == "no":       
            print """As you leave you notice a spigot head that looks as 
                  though it has been broke for a decade. This building 
                  was Not taken care of.
                  """                       
            return "ghetto"      
        else:
            print "Could you repeat that?"
            self.enter()
            
                
class Ghetto(Apartment):

    def enter(self):
        print ex45_entry_desc.ghetto
                 
        question = raw_input("Do you have any questions? > ")
        
        while question != "no":
                   
            if "safe" in question:
                print """Well this ain't Beverly Hills, though I suppose if you
                      could afford Beverly Hills you wouldn't be here. Am I
                      right?
                      """
	    elif "yes" in question:
		print "Great, what would you like to know?"                      
            elif "crime" in question:
                print """Well this ain't Beverly Hills, though I suppose if you
                      could afford Beverly Hills you wouldn't be here. Am I
                      right?
                      """ 
            elif "secure" in question:
                print """Well this ain't Beverly Hills, though I suppose if you
                      could afford Beverly Hills you wouldn't be here. Am I
                      right?
                      """  
            elif "dishwasher" in question:
                print """He laughs. You won't find those kinds of luxuries here. 
                      You have to be realistic about what you can afford. If 
                      you can afford a penthouse apartment then by all means 
                      go for it.
                      """ 
            elif "laundry" in question:
                print """He laughs. You won't find those kinds of luxuries here. 
                      You have to be realistic about what you can afford. If 
                      you can afford a penthouse apartment then by all means 
                      go for it.
                      """ 
            elif "parking" in question:
                print """He laughs. You won't find those kinds of luxuries here. 
                      You have to be realistic about what you can afford. If 
                      you can afford a penthouse apartment then by all means 
                      go for it.
                      """
            elif "bugs" or "break-ins" or "issues" in question:
                print """There were issues in the past but the residents all work 
                      together to make this a nice place to live. It all depends 
                      on who lives here right. If you take care of your 
                      neighborhood, it will take care of you.
                      """
            else:
                print """\"You know, that is a good question.\" He scratches his
                      head then stares off for so long that you realize that 
                      he's completely forgotten your question.
                      """
            question = raw_input("Any other questions? >")
             
        lease = raw_input("Right, well. We ready to sign the lease then? >")
        
        if lease == "no":
            print """You leave. Fresh air washes over you. You finally discern the
                  smell that had hung in that place; it was heavily deodorized 
                  urine.
                  """
            return "our_new_home"                                                                                                             
        elif lease == "yes":
            print ex45_fates.bad_fate
        else:
            print "Come again?"
            self.enter()                     
        
        
class OurNewHome(Apartment):

    def enter(self):
        print ex45_entry_desc.our_new_home

        question = raw_input("Do you have any questions? > ")
        
        while question != "no":
                   
            if "safe" in question:
                print """This is one of the safer neighborhoods in the area."""
	    elif "yes" in question:
		print "Great, what would you like to know?"                
            elif "crime" in question:
                print """There is some crime, being close to downtown. But not a lot.""" 
            elif "secure" in question:
                print """We have never had a break-in."""  
            elif "dishwasher" in question:
                print """Yes, there is a dishwasher.""" 
            elif "laundry" in question:
                print """The washer/dryer maintenence is up to the tenant but those both new units.""" 
            elif "parking" in question:
                print """The unit comes with one assigned space."""
            elif "bugs" or "break-ins" or "issues" in question:
                print """No, this is really an easy-care property for us. It
                      is older and in a slightly less hip part of town but
                      we've never had any problems with it.
                      """
            else:
                print """\"Hmm, I think that's something you'll need to find 
                      out on your own.
                      """
            question = raw_input("Any other questions? >")
             
        lease = raw_input("Great. I brought the lease agreement just in case you fell in love with it. Would you like to sign on? >")
        
        if lease == "no":
            print """You leave. A little sad, either because you are getting
                  tired of the hunt or because you had thought that could
                  be the one.
                  """
            return "closet"                                                                                                             
        elif lease == "yes":
            print ex45_fates.good_fate
        else:
            print "Come again?"                                      
        
                
class Closet(Apartment):

    def enter(self):
        print ex45_entry_desc.closet

        question = raw_input("Do you have any questions? > ")
        
        while question != "no":
                   
            if "safe" in question:
                print """Well, its high visibility so that's gotta count for 
                      something but you aren't moving into the suburbs here
                      you know?
                      """
	    elif "yes" in question:
		print "Great, what would you like to know?"                      
            elif "crime" in question:
                print """Well, its high visibility so that's gotta count for 
                      something but you aren't moving into the suburbs here
                      you know?
                      """ 
            elif "secure" in question:
                print """Yes, you saw the iron gate at the front, we have a buzzer
                      system that we can connect to your cell phone if you
                      prefer. We tell all of the residents not to buzz in anyone
                      that isn't their own guest and to be aware of closing the
                      door after themselves. So yeah, its pretty safe.
                      """  
            elif "dishwasher" in question:
                print """No, theres no way they could fit a dishwasher in here!""" 
            elif "laundry" in question:
                print """Yeah theres a laundry mat two streets over, how easy is that?""" 
            elif "parking" in question:
                print """There are pay lots all over, or you can pay for a pass."""
            elif "bugs" or "break-ins" or "issues" in question:
                print """It really is up to all of the tenants to make this a nice
                      place to live and we do have a good group in here now. 
                      Thats what the owner told me.
                      """
            else:
                print """Hmm, I think that's something you'll need to find 
                      out on your own.
                      """
            question = raw_input("Any other questions? >")
             
        lease = raw_input("Right, well. We ready to sign the lease then? >")
        
        if lease == "no":
            print """You leave. Bummed that you won't be running out to the
                  taco stand at 1 am, but also a little relieved, now where 
				  did you park?
                  """
            return  "bunking_with_strangers"                                                                                                             
        elif lease == "yes":
            print ex45_fates.bad_fate
        else:
            print "Come again?"   
        
class BunkingWithStrangers(Apartment):

    def enter(self):
        print ex45_entry_desc.bunking_with_strangers
              
        choice = raw_input("Do you ring the doorbell? >")
              
        if choice == "yes":
            self.part_2()
        elif choice == "no":
            return "middle_of_nowhere"
        else:
            print "come again?"
            self.enter()

    def part_2(self):
        print ex45_entry_desc.part_2
              
        choice = raw_input("Do you wait? >")
              
        if choice == "no":
            self.lease()
        elif choice == "yes":
            self.roomie()
        else:
            print "Come again?"
            self.next()  

    def lease(self):
        print """Okay. Do you want to sign the lease? I got it ready
              for you, you know, just in case.
              """
              
        choice = raw_input("> ")
        
        if choice == "yes":
            print ex45_fates.bad_fate
        elif choice == "no":
            return "middle_of_nowhere"
        else:
            print "sorry?"
            self.lease()     
            
    def roomie(self):
        print ex45_entry_desc.roomie
        
        question = raw_input("Do you have any questions?  >")
        
        while question != "no":
	  
	  if question == "yes":
	      print "Great, what is your question?"
	  elif question == "How many people live here?":
	      print """7 so far. Three people in the old dining room, a couple in the bedroom
	            and a couple in the coverted attic space.
	            """	  
	  else:
	    print "I'm sorry, I didn't catch that?"
          
          question = raw_input("Do you have any other questions?  >")
          
        lease = raw_input("Do you sign the lease or move on? >")
              
        if lease == "sign the lease":
            ex45_fates.BadFate.bad_fate()
        elif lease == "sign lease":
            ex45_fates.BadFate.bad_fate()
        elif lease == "move on":
            print "It looks like you'll be living out of your car for a while. You lose."
	    exit(1)
        else:
            print "come again?"
            self.roomie()
                                         
        
class Map(object):

    #Dictionary with reference_name:ClassInvocation
    fates = {"evil_landlord":EvilLandlord(),
             "ghetto":Ghetto(),
             "closet":Closet(),
             "bunking_with_strangers":BunkingWithStrangers(),
             "our_new_home":OurNewHome()
             }
              
    def __init__(self, starting_apt):
        #Make incoming variable accessible to following funcs   
        self.starting_apt = starting_apt
        
       
    def ret_fates_name(self, fates_name):
        #Return the val attached to the key 
        val = Map.fates.get(fates_name)
        return val
        
    
    def init_fates_name(self):
        #Instantiate above function using var(starting_apt) as key    
        return self.ret_fates_name(self.starting_apt)     
        



compass = Map("evil_landlord")
motor = Engine(compass)
motor.play()

#