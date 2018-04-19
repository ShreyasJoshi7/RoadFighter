
from gym.envs.registration import registry, register, make, spec

register(
    id='roadfighter-v0',
    entry_point='gym_foo.envs:RoadfighterEnv',
    max_episode_steps=1000,
    reward_threshold=200,
    
)
