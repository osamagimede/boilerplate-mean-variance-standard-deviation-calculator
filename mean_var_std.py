import numpy as np

def calculate(list):
  if len(list) < 9:
      raise ValueError ('List must contain nine numbers.')
  nl=np.array(list)
  print(np.reshape(nl,(3,3)))
  nl=np.reshape(nl,(3,3))
  Calculations = {}
  # Mean
  x= np.mean(nl)
  y= np.mean(nl, axis=0)
  z= np.mean(nl, axis=1)
  y= y.tolist()
  z= z.tolist()
  Calculations['mean']=[y,z,x]
  # Variance
  x= np.var(nl)
  y= np.var(nl, axis=0)
  z= np.var(nl, axis=1)
  y= y.tolist()
  z= z.tolist()
  Calculations['variance']=[y,z,x]
  #Standard deviation
  x= np.std(nl)
  y= np.std(nl, axis=0)
  z= np.std(nl, axis=1)
  y= y.tolist()
  z= z.tolist()
  Calculations['standard deviation']=[y,z,x]
  #Max
  x= np.max(nl)
  y= np.max(nl, axis=0)
  z= np.max(nl, axis=1)
  y= y.tolist()
  z= z.tolist()
  Calculations['max']=[y,z,x]
  #Min
  x= np.min(nl)
  y= np.min(nl, axis=0)
  z= np.min(nl, axis=1)
  y= y.tolist()
  z= z.tolist()
  Calculations['min']=[y,z,x]
  #Sum
  x= np.sum(nl)
  y= np.sum(nl, axis=0)
  z= np.sum(nl, axis=1)
  y= y.tolist()
  z= z.tolist()
  Calculations['sum']=[y,z,x]
  return Calculations