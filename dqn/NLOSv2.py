from Scenario import Scenario
from DQNAgent import DQNAgent
import numpy as np

EPISODES = 2000

if __name__ == "__main__":
    env = Scenario()
    state_size = env.state_size
    action_size = env.action_size
    agent = DQNAgent(state_size, action_size)
    done = False
    batch_size = 32
    for e in range(EPISODES):
        state = env.reset()
        print("Size: " + str(state.shape))
        state = np.reshape(state, [1, state_size])
        time = 0
        done = 0
        while not done:
            action = agent.act(state)
            next_state, reward, done = env.step(action)
            next_state = np.reshape(next_state, [1, state_size])
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if done:
                agent.update_target_model()
                print("episode: {}/{}, score: {}, e: {:.2}"
                      .format(e, EPISODES, time, agent.epsilon))
                break
            time = time + 1
            if time > 2000:
                print("fail to find")
                print("episode: {}/{}, score: {}, e: {:.2}"
                      .format(e, EPISODES, time, agent.epsilon))
                break
        if len(agent.memory) > batch_size:
            agent.replay(batch_size)