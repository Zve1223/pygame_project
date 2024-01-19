from dataclasses import dataclass


@dataclass
class Time:
    fps = 1.0
    tps = 30.0
    delta_time = 1.0 / fps
    fixed_delta_time = 1.0 / tps
    start_time = 0.0
    fixed_update_timer = 0.0
