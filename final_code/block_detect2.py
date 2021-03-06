from task import *

'''
This task operates the magnetic bloc rejection
'''

class Block_Detect(Task):
    def __init__(self,Dim):
        #initialise superobject
        super().__init__(Dim)
        #name
        self.name = 'Block_Detect'

        #flowchart        0            1       2   
        #               idle/accept, reject, block

        #dictionaries represent reaction to trigger based on current state
        self.hall_detect = {
        0 : (('E'),1),          #move forward, goto state 1
        1 : ((),1),             #ignore, stay in state 1
        2: ((),2),
        }
        

        #processing actions
        self.processes = {
        '01' : (self.timeout_hall),
        '10' : (self.open_switch)
        }

        #all possible actions mapped to the corresponding arduino outputs
        self.triggers = {
        '6' : self.hall_detect,
        }

    def timeout_hall(self):
    	#time before block selection switch chosen
        time1 = time.time()
        wait = self.Dim.wait_hall  #how long robot will wait for hall trigger
        func1 = self.reset
        list1 = [time1,wait,func1]
        self.clock_list.append(list1)

    def reset(self):
    	#reset detection after magnetic block rejection timeout
        self.change_state(0)

    def open_switch(self):
    	#reset switch into accepting mode
        self.output.append(self.action_dict['A'])










