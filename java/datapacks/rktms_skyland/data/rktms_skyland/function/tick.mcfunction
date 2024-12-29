# Destroy the sky crystal if it hits water
execute as @e[type=minecraft:snowball,nbt={Item:{components:{"minecraft:item_model":"rktms_skyland:sky_crystal"}}}] at @s if block ~ ~-1 ~ minecraft:water run kill @s

# Make an island if the sky crystal hits non-air and non-water
execute as @e[type=minecraft:snowball,nbt={Item:{components:{"minecraft:item_model":"rktms_skyland:sky_crystal"}}}] at @s unless block ~ ~-1 ~ minecraft:air run function rktms_skyland:_do_crystal
