class CfgPatches
{
	class DZ_Gear_Books
	{
		units[]={
		    "PornBook"
        };
		weapons[]={};
		requiredVersion=0.1;
		requiredAddons[]=
		{
			"DZ_Data"
		};
	};
};
class CfgVehicles
{
	class Book_Base;
	class ItemBook;

	class PornBook: ItemBook
	{
		scope=2;
		title="Les joies de la sodomie";
		author="Toujours plus loin, toujours plus fort";
		displayName="Les joies de la sodomie";
		descriptionShort="Toujours plus loin, toujours plus fort";
		rotationFlags=1;
		hiddenSelectionsTextures[]=
		{
			"ModSource\data\book_bible_co.paa"
		};
	};
};
