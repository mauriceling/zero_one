"""!
ZeroOne (also known as Machine City) - The Simulator / Matrix

Date created: 15th August 2021
"""

import importlib
import sys
import time

environmentBag = {}
programBag = {}
architectCode = []
architectCodeMap = {}
glitch = []

delay = 0

def SUReporter(program, environment, programBag=programBag, 
    environmentBag=environmentBag):
    """!
    Super user function to reports the overall status of the simulation.

    @param program: Function (program) to execute.
    @type program: Callable
    @param environment: Parameters for the program.
    @type environment: Dictionary
    @param programBag: All the functions (programs) in the simulation.
    @type programBag: Dictionary
    @param environmentBag: Parameters for all the functions (programs) 
    in the simulation.
    @returns: environment
    """
    print("Timecycle = %i" % timecycle)
    print("Program Bag = %s" % programBag)
    print("Environment Bag = %s" % environmentBag)
    print("Glitches = %s" % glitch)
    print("Architect Code IDs = %s" % architectCode)
    print("Architect Code Map = %s" % architectCodeMap)
    print("")
    return environment

def SUProgramAdder(program, environment, programBag=programBag, 
    environmentBag=environmentBag):
    """!
    Super user function to add a function (program) into the simulation.

    @param program: Function (program) to execute.
    @type program: Callable
    @param environment: Parameters for the program.
    @type environment: Dictionary
    @param programBag: All the functions (programs) in the simulation.
    @type programBag: Dictionary
    @param environmentBag: Parameters for all the functions (programs) 
    in the simulation.
    @returns: environment
    """
    try: newProgramID = max(programBag.keys()) + 1
    except ValueError: newProgramID = 1
    programBag[newProgramID] = program
    environmentBag[newProgramID] = environment
    environment = {'newProgramID': newProgramID}
    return environment
    
def SUArchitect(program, environment, programBag=programBag, 
    environmentBag=environmentBag):
    """!
    Super user function to add privileged (architect) functions 
    (program) the simulation.

    @param program: Function (program) to execute.
    @type program: Callable
    @param environment: Parameters for the program.
    @type environment: Dictionary
    @param programBag: All the functions (programs) in the simulation.
    @type programBag: Dictionary
    @param environmentBag: Parameters for all the functions (programs) 
    in the simulation.
    @returns: environment
    """
    importlib.reload(sim_architect)
    for ID in [ID for ID in sim_architect.archCode.keys() 
               if ID not in architectCode]:
        environment = SUProgramAdder(sim_architect.archCode[ID], 
                                     sim_architect.archEnv[ID])
        architectCode.append(ID)
        architectCodeMap[ID] = environment['newProgramID']
    return environment   

def SUMaintenance(programBag, environmentBag, architectCode,
    architectCodeMap, glitch):
    """!
    Super user function activate interactive maintainence functions of 
    the simulation.

    @param program: Function (program) to execute.
    @type program: Callable
    @param environment: Parameters for the program.
    @type environment: Dictionary
    @param programBag: All the functions (programs) in the simulation.
    @type programBag: Dictionary
    @param environmentBag: Parameters for all the functions (programs) 
    in the simulation.
    @returns: (programBag, environmentBag, architectCode, 
    architectCodeMap, glitch)
    """
    importlib.reload(sim_maintenance)
    return sim_maintenance.main(programBag, environmentBag,
        architectCode, architectCodeMap, glitch)

if __name__ == "__main__":
    exec("import %s as sim_architect" % sys.argv[1])
    exec("import %s as sim_maintenance" % sys.argv[2])
    try: timecycle = int(sys.argv[3])
    except: timecycle = 1
    SUProgramAdder(SUArchitect, None)
    SUProgramAdder(SUReporter, None)
    # -----------------------------------------------------------------
    # Simulator code
    # -----------------------------------------------------------------
    while True:
        programIDs = list(programBag.keys())
        for ID in programIDs:
            try:
                environmentBag[ID] = \
                    programBag[ID](programBag[ID], environmentBag[ID])
            except:
                if ID not in glitch: glitch.append(ID)
        if sim_architect.simulation_maintenance:
            (programBag, environmentBag, architectCode, 
                architectCodeMap, glitch) = SUMaintenance(programBag, 
                environmentBag, architectCode, architectCodeMap, glitch)
        delay = sim_architect.loop_delay
        time.sleep(delay)
        timecycle = timecycle + 1
    # -----------------------------------------------------------------
    # End of Simulator code
    # -----------------------------------------------------------------
