import json
from infra import onAmbient, onMH_Z19
from base import etl

if __name__ == '__main__':
  with open('settings.json', "r") as f:
    settings = json.load(f)

  channelId = settings['channelId']
  readKey = settings['readKey']
  writeKey = settings['writeKey']

  onAmbient = onAmbient.Ambient(channelId=channelId, writeKey=writeKey, readKey=readKey)
  onMH_Z19 = onMH_Z19.MH_Z19()

  etl.Base(src=onMH_Z19, dest=onAmbient).execute()



