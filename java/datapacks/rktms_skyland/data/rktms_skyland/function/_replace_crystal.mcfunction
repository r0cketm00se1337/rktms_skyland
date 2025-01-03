# Create a new sky crystal at current position with an area effect attached
summon minecraft:snowball ~ ~ ~ {Item:{id:"minecraft:snowball",Count:1b,components:{"minecraft:item_model":"rktms_skyland:sky_crystal"}},Tags:["sc", "sc_init"], Passengers: [{id: "minecraft:area_effect_cloud",Age:-2147483648,Duration:-1,WaitTime:-2147483648,Tags:["sc_cloud"]}]}

# Set owner and motion based on the calling entity (sky crystal)
data modify entity @e[type=snowball,tag=sc_init,limit=1] Owner set from entity @s Owner
data modify entity @e[type=snowball,tag=sc_init,limit=1] Motion set from entity @s Motion

# Remove the init tag from the copied crystal
tag @e[type=snowball,tag=sc_init,limit=1] remove sc_init

# Remove the original sky crystal as it has been replaced
kill @s