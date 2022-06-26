import gym
env = gym.make('MountainCar-v0')
num_episodes = 20
# Uncomment following line to save video of our Agent interacting in this environment
# This can be used for debugging and studying how our agent is performing
# env = gym.wrappers.Monitor(env, './video/', force = True)

# Number of times you want to train your agent to achieve the goal
# Equivalent to number of epochs.
env.reset()
for i in range(0, num_episodes):
    t = 0
    while True:
        t += 1
        env.render()
        # print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
