label door_open:
    "Cosmo reaches for the door handle, half expecting to see his brother's apartment inside."
    "Instead what he saw shocked him to his very core, a monster stood waiting on the other side of the door, one with a wide grin on its face, the very fabric of reality rippling around him."
    hide doorclosed
    show dooropengif at right
    hide cosmoneutralgif
    show cosmoscared1 at left
    c "Wha.. what's that thing??"
    "???" "olHel eterh, my twah a aedohmns caef oyu veha eehrt he.ehe It si tno eyrvdaye I ese a vinilg sponre re.eh"
    c "Huh, I can not understand you at all, what did you do to my brother??"
    c "Please tell me he's ok...."
    hide cosmoneutralgif
    hide cosmoscared1
    show cosmoscared at left
    "???" ",hO het belu dehira o,ne he datste cien nda ym.yum eH amce hutogrh eher a tbi oga btu eh was ont sa rnea enci niklgoo as y!uo"
    "???" "Yuo llems kile g,iacm a lehwo ndanbcuae of it ehe.eh I tbe if I klil ouy i acn aosbbr all ttha ciagm esindi uyo nda nteh I iwll eb ebla to sepaec tshi nald eonc nad ofr all!"
    hide cosmoscared
    show cosmohorrified at left
    "As Cosmo stood there with his legs unable to move, he could feel the tendrils wrapping around his legs, he grasped at them trying to pry himself free but to no avail."
    "This thing had too much of a grip on him, that he could not wiggle himself loose from the monster. It started to pull Cosmo towards it, a look of pure horror glazing over his face as he watched his whole life flash before his eyes."
    "Stupid, to think he didn't even get to achieve his goals yet, to think he did't get to say goodbye to tenders, let alone spend his last moments with those he loved."
    hide cosmohorrified
    show cosmohorrified1 at left
    c "Ji-Hu, i'm so sorry.... I wish there was more I could have done to help you...."
    c "Please do not forget me, I love you brother."
    scene black with dissolve

    show text "Ending 1 out of 8: Deaths Door" with Pause(1.5)

    scene black with dissolve
    return
label backdoor:
    scene bg backdoor
    with fade
    "Not wanting to risk the door in front of him, he walks towards the backdoor which he has used to sneak into his brother's place before."
    hide doorclosed
    "Reaching for the doorknob, he opens the door up revealing the back hallway that leads into the library and living room area."
    "He could hear some noises coming from the library, but he knew he needed to be careful as he never knew when monsters would be lurking in the area."
    hide cosmohorrified1
    show cosmotalkgif at left
    c "Hello? Is anyone there?."
    c "Ji-Hu? Sherbet?"
    hide cosmotalkgif
    show cosmoneutralgif
    "With no answer, there was no choice but to look around. Not sure if the noise was a creature or if somehow it was someone who had not heard him yell down the hall."
menu brothers_house:
        "Bedroom.":
            jump brothersbedroom
        "Office.":
            jump office
        "Library.":
            jump library
        "Bathroom.":
            jump brothersbathroom
        "Kitchen.":
            jump brotherskitchen
