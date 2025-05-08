from pointmaze import GridWorldEnv

env = GridWorldEnv(render_mode="human",size=11)
obs, _ = env.reset()

while(True):
    action = env.action_space.sample()
    obs, reward, done, _, _ = env.step(action)
    env.render()
    if done:
        print("Goal reached!")
        break

env.close()
