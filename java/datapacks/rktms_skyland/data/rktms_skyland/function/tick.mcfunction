# Destroy the sky crystal if it hits water
execute as @e[tag=sc_cloud] at @s if block ~ ~1 ~ minecraft:water run kill @s
execute as @e[tag=sc_cloud] at @s if block ~ ~ ~ minecraft:water run kill @s
execute as @e[tag=sc] at @s if block ~ ~1 ~ minecraft:water run kill @s
execute as @e[tag=sc] at @s if block ~ ~ ~ minecraft:water run kill @s

# If a sky crystal is thrown replace it with a tagged version and
# an area_effect_cloud to track where it hits
execute as @e[type=minecraft:snowball,tag=!sc,nbt={Item:{components:{"minecraft:item_model":"rktms_skyland:sky_crystal"}}}] at @s run function rktms_skyland:_replace_crystal

# If any crystals have hit the ground, create a sky island
execute as @e[type=minecraft:area_effect_cloud,tag=sc_cloud] at @s unless predicate rktms_skyland:in_flight unless block ~ ~ ~ minecraft:water unless block ~ ~1 ~ minecraft:water unless block ~ ~-1 ~ minecraft:water run function rktms_skyland:_do_crystal
