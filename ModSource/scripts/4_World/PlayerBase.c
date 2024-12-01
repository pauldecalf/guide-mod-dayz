// PlayerBase.c le script pour mettre un message dans la console chaque fois que le joueur saute.

class ModSource: MissionGameplay
{
    void ModSource()
    {
        Print("ModSource::ModSource");
    }

    override void OnJumpStart()
    {
        Print("ModSource::OnJumpStart");
    }
};

Mission CreateCustomMission(string path)
{
    return new ModSource();
}
