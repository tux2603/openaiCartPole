import gym

env = gym.make('CartPole-v0')

for _ in range(20):

    observation = env.reset()

    for t in range(100):

        # env.render()
        action = env.action_space.sample()

        print(f'for {observation}, taking action {action}')

        observation, reward, done, info = env.step(action)
        
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break

env.close()