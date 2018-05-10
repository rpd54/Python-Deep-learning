import gym
env = gym.make('MountainCar-v0')
observation = env.reset()
print("observation=",observation)
for t in range(100):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print("observation=",observation)
    print("reward=",reward)
    print("done=",done)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break