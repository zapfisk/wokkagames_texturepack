name = input("name: ")

with open("items/" + name + ".json", "w") as f:
    f.write('{\n')
    f.write('	"model": {\n')
    f.write('		"type": "minecraft:model",\n')
    f.write('		"model": "rauch:item/' + name + '"\n')
    f.write('	}\n')
    f.write('}\n')

with open("models/item/" + name + ".json", "w") as f:
    f.write('{\n')
    f.write('	"parent": "item/handheld",\n')
    f.write('	"textures": {\n')
    f.write('		"layer0": "rauch:item/' + name + '"\n')
    f.write('	}\n')
    f.write('}\n')
