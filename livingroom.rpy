#start chapter 1
label living_room:
    scene black with dissolve

    show text "Chapter 1:Search" with Pause(1.5)

    scene black with dissolve

    scene bg livingroom
    with fade
    "Heading back to the living room, Cosmo sits down on the couch. His eyes slowly drift off to sleep as he sits on the couch with the tv turned on to his favorite show."

    "A few hours later, he opens his eyes, but something feels off."
    scene bg livingroomdark
    with fade
    "He was just asleep, but now his apartment looks strange."

    "What was going on? Was he going crazy?"

    show cosmotalkgif at left

    c "Huh, am I dreaming? i've got to be right."

    c "There was not a sky outside my window before I went to sleep, let alone one that looked like it was staring at me."
    scene bg window2
    with fade
    "Outside his window was no longer the city view he once knew all too well, instead was a sight unlike any other."

    "It was almost like he'd traveled from earth, up into some other dimension. He could almost see the stars for a split second."

    "Where was this place? Was he in space?"
    scene bg livingroomdark
    with fade
    hide cosmotalkgif

    show cosmothinktalkgif at left

    c "Now, let's think this through. The only explanation of this phenomenon is that it is a manifestation of my visions."
    c "Where's Ji-Hu when I need him?"
    c "Maybe I should go see him, to see if he has a book that can help explain what it was that is going on."
    hide cosmothinktalkgif
    show cosmothinkgif at left
    scene bg corridor
    with fade
    "Stepping outside, he looked up at the sky, one could almost make out the shape of some creature in the sky."
    "It was massive but for some reason, as cosmo looked up at it it seemed to be distorted and blurry."
    "That could not have been himself could it? That was impossible, but it would explain why despite everything he could only make out the general shape."
    "Walking down the streets of central, there were many spots where if he took one wrong step then Cosmo would end up in the void below."
    "As he kept walking, it felt like something was following him, yet he kept going because if anyone could help him it would be his brother."
    hide cosmothinktalkgif
    show cosmothinkgif at left
    c "What has happened to Guishan? Why me, is this my punishment for everything i've ever done wrong...."
    c "Please Ji-Hu be ok, I do not want you to be hurt because of what I did to all those people..."
    hide cosmothinktalkgif
    show cosmothinkgif at left
    c2 "What are you doing here young child, you do not belong here wandering this endless maze."
    hide cosmothinkgif
    show cosmothinktalkgif at left
    c "Maze? If you say this is a maze, then surely you know what this place is?"
    hide cosmothinktalkgif
    show cosmothinkgif at left
    c2 "It is a place where things live that do not exist in your world, like the monsters under your bed that your parents claimed were not real."
    hide cosmothinkgif
    show cosmothinktalkgif at left
    c "But those things do not exist, if they did I would have seen them before, but how did I end up here though? Earlier I saw something in a client's future that should not have been there, did it come from here?"
    hide cosmothinktalkgif
    show cosmothinkgif at left
    c2 "I do not know how you got here, nor do I know if what you saw came from here. In fact I myself am just a projection of a version of you, though it is likely you will run into other versions of yourself as well elsewhere."
    scene bg nachoshousedoor
    with fade
    hide cosmothinktalkgif
    show cosmoneutralgif at left

    "A few minutes later, Cosmo arrived at his brother's house, but there was something off about the door leading to his brother's house."
    show doorclose at right
menu door_choice:
    "Open":

        jump door_open

    "Leave it alone.":

        jump backdoor
