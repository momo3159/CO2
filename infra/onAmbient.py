import ambient

class Ambient:
  def __init__(self, channelId, writeKey, readKey):
    self.am = ambient.Ambient(channelId, writeKey, readKey)


def send(self, value):
  try:
    self.am.send(value)
  except:
    raise Exception("can't send value to ambeint at Ambient.send")