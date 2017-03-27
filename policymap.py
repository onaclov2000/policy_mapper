import Image, ImageDraw
import os
import numpy as np
import math
class PolicyMap:
   def __init__(self, size, name):
      self.height = size[0]
      self.width  = size[1]
      self.images = {}
      for i in os.listdir("images"):
         self.images[i.strip('.png')] = Image.open('images/' + i)
      self.out  = Image.new('RGB', (self.width * 50, self.height * 50))
      self.name = name
      #images = map(Image.open, ['images/d.png', 'dl.jpg', 'Test3.jpg'])
      
   def draw(self, policy, actions = {0 : 'u', 1: 'r', 2 : 'd', 3 : 'l'}):
      
      for i in range(policy.shape[0]):
         tmp = np.where(policy[i] ==np.max(policy[i]))
         res = []
         
         for j in range(len(tmp[0])):
            res.append(actions[tmp[0][j]])
#         print "NEXT", i, self.height, self.width, (i%self.height*50,)
         self.out.paste(self.images[''.join(sorted(res))], (i%self.height*50,int(math.floor(i/self.width))*50))
         draw = ImageDraw.Draw(self.out)
         draw.rectangle((i%self.height*50, int(math.floor(i/self.width))*50, i%self.height*50 + 49,int(math.floor(i/self.width))*50 +49), fill=None, outline='#000000')
         #(pos[0] * offset) + pos[1]
      self.out.save(self.name)
            
if __name__ == "__main__":
   p = PolicyMap((2,2), '2x2.png')
   #Q = np.random.uniform(-1., 1.0, (4, 4))
   Q = np.array([[-1,0,0,0],
                 [0,0,-1,-1],
                 [-1,0,-1,-1],
                 [-1,-1,-1,-1]], dtype=np.float32)
   p.draw(Q)
   
      



