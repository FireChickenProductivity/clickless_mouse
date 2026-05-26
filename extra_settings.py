from talon import Module

mod = Module()

mod.setting(
	"clickless_mouse_fire_chicken_moving_sensitivity",
	type=int,
	default=0,
	desc="The amount to move the cursor before it is not considered dwelling"
)