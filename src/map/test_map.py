import mujoco
import numpy as np

# Charger le modèle
model = mujoco.MjModel.from_xml_path("pointmaze_impasse.xml")
data = mujoco.MjData(model)

# Initialiser le renderer avec une fenêtre affichable
renderer = mujoco.Renderer(model)

# Simulation et rendu
data.ctrl[:] = [1.0, 1.0]
for _ in range(100):
    mujoco.mj_step(model, data)
    renderer.update_scene(data)
    renderer.render_to_window()  # Affiche dans une fenêtre
