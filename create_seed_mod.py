import os

def create_seed_mod_structure(mod_name="custom_seed_mod"):
    # Définir la structure des dossiers et fichiers
    structure = {
        mod_name: {
            "config.cpp": """\
class CfgPatches
{
    class custom_seed_mod
    {
        units[] = { "PurpleWeedSeeds" };
        weapons[] = {};
        requiredVersion = 0.1;
        requiredAddons[] = { "DZ_Data" };
    };
};

class CfgVehicles
{
    class CannabisSeeds;
    class PurpleWeedSeeds: CannabisSeeds
    {
        scope = 2;
        displayName = "Purple Weed Seeds";
        descriptionShort = "Purple Weed Seeds for cultivation.";
        description = "High-quality Purple Weed Seeds.";
        model = "\\dz\\gear\\cultivation\\cannabis_seeds.p3d";
        rotationFlags = 17;
        hiddenSelections[] = { "zbytek" };
        hiddenSelectionsTextures[] = { "custom_seed_mod\\data\\weed_seeds_co.paa" };
        weight = 5;
        itemSize[] = { 1, 1 };
    };
};
""",
            "data": {
                "weed_seeds_co.paa": "Texture file placeholder (replace with actual .paa texture)",
            },
            "scripts": {
                "4_World": {
                    "entities": {
                        "items": {
                            "seeds": {
                                "PurpleWeedSeeds.c": """\
class PurpleWeedSeeds extends CannabisSeeds
{
    override void SetActions()
    {
        super.SetActions();
        AddAction(ActionPlantSeed); // Allows planting
    }
};
"""
                            },
                        },
                    },
                },
            },
        },
    }

    # Fonction pour créer les fichiers et dossiers
    def create_structure(base_path, structure):
        for key, value in structure.items():
            path = os.path.join(base_path, key)
            if isinstance(value, dict):
                # Créer les sous-dossiers
                os.makedirs(path, exist_ok=True)
                create_structure(path, value)
            else:
                # Créer les fichiers avec le contenu
                with open(path, "w") as file:
                    file.write(value)

    # Dossier de base du mod
    base_path = os.path.join(os.getcwd(), mod_name)
    create_structure(base_path, structure)
    print(f"Mod structure created successfully in: {base_path}")

# Lancer le script
create_seed_mod_structure()
