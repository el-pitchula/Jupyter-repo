import random
import gym
import numpy as np

env = gym.make("CartPole-v1", render_mode="human")

episodes = 1000
for episode in range(1, episodes + 1):
    state, _ = env.reset()  # Agora env.reset() retorna dois valores: state e info
    done = False
    score = 0

    while not done:
        action = random.choice([0, 1])
        observation, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated  # O episódio pode terminar por terminated ou truncated
        score += reward
        env.render()
    print(f"Episode: {episode}, Score: {score}")
env.close()
