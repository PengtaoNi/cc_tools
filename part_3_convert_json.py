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
        level.level_number = json_level["level_number"]
        level.time = json_level["time"]
        level.num_chips = json_level["num_chips"]
        level.upper_layer = json_level["upper_layer"]

        for json_field in json_level["optional_fields"]:
            field_type = json_field["field_type"]
            if field_type == "title":
                title_field = cc_classes.CCMapTitleField(json_field["title"])
                level.add_field(title_field)
            elif field_type == "pw":
                pw_field = cc_classes.CCEncodedPasswordField(json_field["pw"])
                level.add_field(pw_field)
            elif field_type == "hint":
                hint_field = cc_classes.CCMapHintField(json_field["hint"])
                level.add_field(hint_field)
            elif field_type == "monster":
                monsters = []
                for json_monster in json_field["monsters"]:
                    x = json_monster["x"]
                    y = json_monster["y"]
                    monster_coord = cc_classes.CCCoordinate(x, y)
                    monsters.append(monster_coord)
                monster_field = cc_classes.CCMonsterMovementField(monsters)
                level.add_field(monster_field)

        level_pack.add_level(level)

    return level_pack

with open("data/pni_cc1.json", "r") as reader:
    json_data = json.load(reader)
    level_pack = make_level_pack_form_json(json_data)
    print(level_pack)

cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "data/pni_cc1.dat")