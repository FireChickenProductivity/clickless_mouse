from talon import settings

import math

def is_dwelling(
	original_x: int,
	original_y: int,
	current_x: int,
	current_y: int
) -> bool:
	sensitivity = settings.get("user.clickless_mouse_fire_chicken_moving_sensitivity")
	return (math.fabs(original_x - current_x) <= sensitivity) and \
		(math.fabs(original_y - current_y) <= sensitivity)

def is_no_longer_idle(
	original_x: int,
	original_y: int,
	current_x: int,
	current_y: int
) -> bool:
	sensitivity = settings.get("user.clickless_mouse_fire_chicken_moving_sensitivity")
	return (math.fabs(original_x - current_x) > sensitivity + 1) or \
		(math.fabs(original_y - current_y) > sensitivity + 1)