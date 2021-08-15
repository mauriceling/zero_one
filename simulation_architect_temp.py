archCode = {}
archEnv = {}
loop_delay = 10
simulation_maintenance = False
# ---------------------------------------------------
def architect(program, environment):
    return environment
architectE = {'identity': 'architect',
              'passcode': 'iamtheboss'}
              
archCode = \
{0: architect,}

archEnv = \
{0: architectE,}

loop_delay = 10
simulation_maintenance = False
# ---------------------------------------------------
def architect(program, environment):
    return environment
architectE = {'identity': 'architect',
              'passcode': 'iamtheboss'}

def oracle(program, environment):
    return environment
oracleE = {'identity': 'oracle',
              'passcode': 'ilovefood'}

archCode = \
{0: architect,
1: oracle}

archEnv = \
{0: architectE,
1: oracleE}

loop_delay = 10
simulation_maintenance = False

