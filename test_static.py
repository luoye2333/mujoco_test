import time
import numpy as np
import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path("test2.xml")
model.opt.timestep = 0.02
data = mujoco.MjData(model)

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
