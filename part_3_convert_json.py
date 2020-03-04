import cc_dat_utils
import cc_classes
import json

#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file

def make_level_pack_form_json(json_data):
    level_pack = cc_classes.CCLevelPack()

    for json_level in json_data["levels"]:
        level = cc_classes.CCLevel()
        level.level_number = json_level["level_number"]+1
        level.time = json_level["time"]
        level.num_chips = json_level["chip_number"]
        level.upper_layer = json_level["upper_layer"]

        fields = json_level["optional_fields"]
        for field in fields:
            if field == "map title":
                title_field = cc_classes.CCMapTitleField(fields[field])
                level.add_field(title_field)
            elif field == "encoded password":
                pw_field = cc_classes.CCEncodedPasswordField(fields[field])
                level.add_field(pw_field)
            elif field == "hint text":
                hint_field = cc_classes.CCMapHintField(fields[field])
                level.add_field(hint_field)
            elif field == "moving objects":
                monsters = []
                for json_monster in fields[field]:
                    x = json_monster[0]
                    y = json_monster[1]
                    monster_coord = cc_classes.CCCoordinate(x, y)
                    monsters.append(monster_coord)
                monster_field = cc_classes.CCMonsterMovementField(monsters)
                level.add_field(monster_field)

        level_pack.add_level(level)

    return level_pack

# with open("data/pni_cc1.json", "r") as reader:
with open("data/pni_cc_level_data.json", "r") as reader:
    json_data = json.load(reader)
    level_pack = make_level_pack_form_json(json_data)
    print(level_pack)

cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "data/pni_cc_level_data.dat")