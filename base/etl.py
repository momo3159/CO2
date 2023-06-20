from datetime import datetime

class Base:
  def __init__(self, src, dest):
    self.src = src
    self.dest = dest

  def execute(self):
    co2 = self.src.getCO2()
    createdAt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.dest.send({'created': createdAt, 'co2': co2})

