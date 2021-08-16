"""!
ZeroOne (also known as Machine City) - Machine City Native Maintenance 
Code

Date created: 15th August 2021
"""

def do_pause(cmd, programBag, environmentBag, architectCode, architectCodeMap, glitch):
    import time
    print("// Pause %i" % int(cmd[1]))
    time.sleep(int(cmd[1]))
    return (programBag, environmentBag, architectCode, architectCodeMap, glitch)

def processor(cmd, programBag, environmentBag,
              architectCode, architectCodeMap, glitch):
    if cmd[0] == "pause":
        return do_pause(cmd, programBag, environmentBag, architectCode, architectCodeMap, glitch)

def main(programBag, environmentBag,
         architectCode, architectCodeMap, glitch):
    cmd = input("// Maintenance Command: ")
    cmd = [x.lower() for x in cmd.split(" ")]
    try:
        (programBag, environmentBag, architectCode, architectCodeMap, glitch) = \
            processor(cmd, programBag, environmentBag, architectCode, architectCodeMap, glitch)
    except:
        pass
    return (programBag, environmentBag, architectCode, architectCodeMap, glitch)