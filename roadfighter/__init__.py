from gym.envs.registration import register

register(
    id='roadfighter-v0',
    entry_point='gym_foo.envs:RoadfighterEnv',
)
