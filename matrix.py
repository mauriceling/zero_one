"""!
ZeroOne (also known as Machine City) - The Simulator / Matrix

Date created: 15th August 2021
"""

import importlib
import time

import simulation_architect
import simulation_maintenance

environmentBag = {}
programBag = {}

architectCode = []
architectCodeMap = {}

glitch = []

delay = 0

def SUReporter(program=None, environment=None, 
               programBag=programBag, 
               environmentBag=environmentBag):
    print("Timecycle = %i" % timecycle)
    print("Program Bag = %s" % programBag)
    print("Environment Bag = %s" % environmentBag)
    print("Glitches = %s" % glitch)
    print("Architect Code IDs = %s" % architectCode)
    print("Architect Code Map = %s" % architectCodeMap)
    print("")
    return environment

def SUProgramAdder(program=None, environment=None, 
                   programBag=programBag, 
                   environmentBag=environmentBag):
    try: newProgramID = max(programBag.keys()) + 1
    except ValueError: newProgramID = 1
    programBag[newProgramID] = program
    environmentBag[newProgramID] = environment
    environment = {'newProgramID': newProgramID}
    return environment
    
def SUArchitect(program=None, environment=None, 
                programBag=programBag, 
                environmentBag=environmentBag):
    importlib.reload(simulation_architect)
    for ID in [ID for ID in simulation_architect.archCode.keys() 
               if ID not in architectCode]:
        environment = SUProgramAdder(simulation_architect.archCode[ID], 
                                     simulation_architect.archEnv[ID])
        architectCode.append(ID)
        architectCodeMap[ID] = environment['newProgramID']
    return environment   

def SUMaintenance(programBag=programBag, 
                  environmentBag=environmentBag,
                  architectCode=architectCode,
                  architectCodeMap=architectCodeMap,
                  glitch=glitch):
    importlib.reload(simulation_maintenance)
    return simulation_maintenance.main(programBag, 
                                       environmentBag,
                                       architectCode,
                                       architectCodeMap,
                                       glitch)

SUProgramAdder(SUArchitect, None)
SUProgramAdder(SUReporter, None)

timecycle = 1
while True:
    programIDs = list(programBag.keys())
    for ID in programIDs:
        try:
            environmentBag[ID] = \
                programBag[ID](programBag[ID], environmentBag[ID])
        except KeyError:
            if ID not in glitch: glitch.append(ID)
    if simulation_architect.simulation_maintenance:
        newEnv = SUMaintenance(programBag, environmentBag,
                architectCode, architectCodeMap, glitch)
        programBag = newEnv[0] 
        environmentBag = newEnv[1]
        architectCode = newEnv[2]
        architectCodeMap = newEnv[3]
        glitch = newEnv[4]
    delay = simulation_architect.loop_delay
    time.sleep(delay)
    timecycle = timecycle + 1
