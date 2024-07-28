
import numpy as np
from utils2 import read_canonical_model, load_pc, visualize_icp_result

from icp import ICP
if __name__ == "__main__":
  obj_name = 'drill' # drill or liq_container
  num_pc = 4 # number of point clouds

  #source_pc = read_canonical_model(obj_name)
  icp_object = ICP(40)
  
  for k in range(1):
    source_pc = read_canonical_model(obj_name)
    for i in range(4):
      target_pc = load_pc(obj_name, i)
      #print(target_pc.shape)
      # estimated_pose, you need to estimate the pose with ICP
      pose = np.eye(4) 
      R_init = np.eye(3)
      if obj_name == 'drill' and i > 1:
      #if i > 1:
        R_init = np.array([[-1,0,0],[0,-1,0],[0,0,1]])
      P_init = np.mean(target_pc, axis = 0) - np.mean(source_pc, axis = 0)
      P_init = P_init.reshape(1,-1)
      R, P = icp_object.getRP(source_pc, target_pc, R_init,P_init)
      pose[0:3, 3] = P
      pose[0:3, 0:3] = R 
      print(pose)
      # visualize the estimated result
      
      visualize_icp_result(source_pc, target_pc, pose)

