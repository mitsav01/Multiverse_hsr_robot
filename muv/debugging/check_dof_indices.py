import mujoco
import mujoco_viewer

# Load your XML model (adjust path as needed)
model = mujoco.MjModel.from_xml_path("/home/akshay/Multiverse/Multiverse-Resources/robots/hsr_robot/hsr_mujoco/model/hsrb4s.xml")

print("Joint indices and names:")

for i in range(model.njnt):
    joint_name = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_JOINT, i)
    print(f"- {joint_name}")

