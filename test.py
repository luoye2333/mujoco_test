import time
import numpy as np
import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path("test.xml")
model.opt.timestep = 0.02
data = mujoco.MjData(model)


# path = "stair_up.npy"
path = "stair_down.npy"
vertical_scale = 0.005
real_height = np.load(path) * vertical_scale

model.hfield_data = real_height.transpose().flatten() # penetrate
# model.hfield_data = real_height.transpose().flatten() * 10 # penetrate more, NOTE: remember to change test.xml
# model.hfield_data = real_height.transpose().flatten() * 0.1 # ok
# model.hfield_data = real_height.transpose().flatten() - 2.0 # ok

viewer = mujoco.viewer.launch_passive(model, data)
viewer.cam.distance = 10.0  # 摄像机距离

count = 0
while viewer.is_running():
    mujoco.mj_step(model, data)
    if count > 100:
        mujoco.mj_resetData(model, data)
        count = 0
    count += 1
    time.sleep(1/50.)
    viewer.sync()

viewer.close()
