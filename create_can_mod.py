import os

def create_mod_structure(mod_name="custom_food"):
    # Définir la structure des dossiers
    structure = {
        mod_name: {
            "data": {
                "drinks": {
                    "data": {
                        "sodacan_whoopass_co.paa": "Texture file placeholder (replace with actual texture)",
                    },
                    "config.cpp": """\
class CfgPatches
{
    class custom_soda
    {
        units[]= { "custom_soda_can" };
        weapons[]={};
        requiredVersion=0.1;
        requiredAddons[]= { "DZ_Data" };
    };
};

class CfgVehicles
{
    class SodaCan_ColorBase;
    class custom_soda: SodaCan_ColorBase
    {
        scope=2;
        displayName="Whoopass";
        descriptionShort="Whoopass is a carbonated soft drink that is the favorite drink of the character Duke Nukem. It is a parody of the real-life energy drink Red Bull.";
        hiddenSelectionsTextures[]= { "custom_food\\data\\drinks\\data\\sodacan_whoopass_co.paa" };
        class Nutrition
        {
            fullnessIndex=100;
            energy=1000;
            water=1000;
            nutritionalIndex=100;
            toxicity=0;
        };
    };
};
""",
                },
            },
            "scripts": {
                "4_World": {
                    "entities": {
                        "itembase": {
                            "Edible_Base": {
                                "custom_soda.c": """\
class custom_soda extends Edible_Base
{
    override bool CanBeCooked()
    {
        return true;
    }

    override bool CanBeCookedOnStick()
    {
        return false;
    }

    override bool IsMeat()
    {
        return false;
    }

    override bool CanDecay()
    {
        return false;
    }

    override void SetActions()
    {
        super.SetActions();
        AddAction(ActionDrink);
    }
};
"""
                            },
                        },
                    },
                },
            },
            "config.cpp": """\
class CfgPatches
{
    class custom_food
    {
        units[]= { "custom_soda_can" };
        weapons[]={};
        requiredVersion=0.1;
        requiredAddons[]= { "DZ_Data" };
    };
};

class CfgMods
{
    class custom_food
    {
        dir = "custom_food";
        name = "Custom Food Mod";
        credits = "Your Name";
        author = "Your Name";
        version = "1.0";
        type = "mod";
        dependencies[] = { "World" };

        class defs
        {
            class worldScriptModule
            {
                value = "";
                files[] = { "custom_food/scripts/4_World" };
            };
        };
    };
};
""",
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
create_mod_structure()
