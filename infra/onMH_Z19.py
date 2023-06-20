import mh_z19

class MH_Z19:
  def __init__(self):
    pass

def getCO2() -> int:
  measurements = mh_z19.read()

  if 'co2' in measurements:
    return measurements['co2']
  else:
    raise Exception("can't get CO2 value at getCO2.")
