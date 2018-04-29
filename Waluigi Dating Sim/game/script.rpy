define m = Character(_("Maria"), color="#f79b9b")
define w = Character("Waluigi")

define slowdissolve = Dissolve(1.0)


# The game starts here.

label start:

    play music "pinball.mp3"
    #stop music fadeout 1


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    python:
        name = renpy.input("What's your name?")
        name = name.strip()

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    define e = Character(_("[name]"), color="#7ad4ef")

    # These display lines of dialogue.
    "You are the school's 'Ask Alice'."
    "People send you peculiar questions all the time and you give advice in return."
    "One day, you get a PARTICULARLY peculiar request: to help Maria in her pursuit for a new boy
    at your school named Waluigi."

    scene yard
    show maria
    with slowdissolve

    m "Hey [name], I need some help with something."
    e "Lay it on me. Please don't tell me you have an essay due in an hour."
    m "Have you heard about that new boy at school?"
    menu:
        "Sure I have. Just don't quiz me on it.":
            jump newboi_yes
        "Not at all. Should I be concerned?":
            jump newboi_no
    label newboi_yes:
        $ menu_flag = True
        m "Quiz or not, I must find out more about him!"
        e "Sounds riveting. Please don't tell me you have a research project due in an hour."
        m "He's so dreamy. He makes my knees weak."
        menu:
            "So he makes you sleepy?":
                jump sleepy_yes
            "Elephant tranquilizer has the same effect.":
                jump sleepy_no
        label sleepy_yes:
            $ menu_flag = True
            m "Quite the opposite. Thinking about him keeps me awake at night!"
            jump sleepy_done
        label sleepy_no:
            $ menu_flag = False
            m "He's more of a morphine kind of guy. You fall for him instantly."
            e "That's an... interesting metaphor."
            jump sleepy_done
        label sleepy_done:
        jump newboi_done
    label newboi_no:
        $ menu_flag = False
        m ";3"
        e "Owo?"
        m ";^)"
        e "Oh, it's *THAT* kind of situation."
        m "So, what do you say? Think you can help me?"
        e "I've got this. He'll be gone in no time."
        m "What?! No! I'm asking for dating advice. What are you talking about?"
        menu:
            "Oh, I get those requests regularly. You know how group projects end up.":
                jump advice_yes
            "Hah oops! My autocorrect is on. Silly mistake, go on...":
                jump advice_no
        label advice_yes:
            $ menu_flag = True
            m "I can relate."
            jump advice_done
        label advice_no:
            $ menu_flag = False
            m "We're talking face to face."
            jump advice_done
        label advice_done:
        jump newboi_done
    label newboi_done:
    e "So what about this new kid is so special? I mean ---"
    m "Oh my! He's coming over right now."
    e "You know what I say about situations like these."
    m "The more the merrier?"
    e "Three's a crowd."



    play music "Tacostand.mp3"




###SCENE 2

    scene black
    with slowdissolve

    "Ever since that day, Maria has been asking me to help her get close to Waluigi... by any means possible"
    "Which includes stalking all forms of social media to get information"
    "According to his twitter, Waluigi is quite the fan of roses... and absolutely HATES cheaters... huh"

    scene classroom
    show maria

    m "Hello!~~"
    m "Have you been doing your homework?"
    menu:
        "I didn't really have a choice my dood":
            jump choice2_yes
        "Haha no":
            jump choice2_no
    label choice2_yes:
        m "That's what I like to hear!"
        jump choice2_done
    label choice2_no:
        show maria mad
        m "Ummmm EXCUSE ME?!?!"
        e "Chill, I was joking. Obviously I did."
        jump choice2_done
    label choice2_done:
    show maria
    m "Soooo what did you find out?"
    e "Well... he likes roses and does NOT like cheaters..."
    show maria mad
    m "Are you YOLKING me? That's all you have?"
    m "How is knowing he dislikes cheaters going to help me slide into his DMs??"
    e "It's not just that, now you know to leave roses by his locker!"
    m "UGHHH what am I paying you for??"
    e "Wait, I'm getting paid?"
    m "Shut up"
    show maria
    m "Anywayyyy, if we want to find out more about Waluigi, you'll have to actually spend some time with him!"
    m "You know, talk to him, get to know him better, find out if he's into girls with thick facial hair..."
    m "Okeee peace"
    hide maria
    scene black
    with fade
    "Ugh, what a pain... I can't believe I'm actually doing this for her!"
    "But... this Waluigi guy IS kind of interesting. I guess finding out more about him isn't the worst thing"
    "I know he's in my chemistry class, and we have a project coming up..."
    "But he doesn't seem the type to enjoy school related things, so I'm not sure how well that would go"
    "Hmm... I think he's also president of the WAH club: Wahnderful Appreciation Club"
    "I don't know HOW he's become president of a club when he just got here but WAHTEVER"
    "He must be quite fond of it, but there aren't many members. In fact, I think there's NONE"
    "What should I do...?"
    menu:
        "Be his partner for a project":
            jump project
        "Join the same club as him":
            jump club
    label project:
        e "Screw it, I don't care if he's unwilling to do a project"
        jump scene3_a
    label club:
        e "If he's fond of his club, and there aren't many members... it seems pretty promising"
        jump scene3_b
#SCENE 3 (A)

    label scene3_a:
        "(The next day...)"
        scene lab
        "Okay, I'm gonna ask him to be my partner."
        stop music fadeout 1
        play music "bill nye.mp3"
        show wah
        e "Hey, Waluigi right?"
        e "Wanna be partners for the upcoming project?"
        show wah happy
        w "Waahhh."
        e "I'm sorry...what?"
        w "Waaaaaah!"
        e "Is...is that a yes?!?"
        show wah mad
        w "Wah!"
        show wah
        "What does she SEE in him??"
        #change the scene here... maybe find a chem lab
        e "Okay... we need to light a bunsen burner. Do you know how to light one?"
        w "Wah."
        e "I don't know how to light one! This garbage school never taught us!"
        w "Waaaaahh?"
        e "Oh my god, fine, I'll do it."
        #So I go to light the bunsen burner, knowing very well this will not end well..."
        #the same lab but there's fire and stuff

        "*FWOOOSH*"
        "*burning noises*"
        show wah sad
        w "wAaAAAAAAHHHH!!!!!!!!!!!"
        e "OH MY GOD!!!"
        #change scene to like classroom or something
        scene fire
        with fade
        "We actually didn't die from that accident, but..."
        "Waluigi's mustache got burned off."
        "Luckily, Maria came running in with a fire extinguisher to save the day."
        scene classroom
        show maria at left
        show wah nostache at right
        w "Wah! Maria, you saved my life! Even though my mustache burned off..."
        show maria happy at left
        m "Don't worry Waluigi! I'll buy you a fake one and you'll look as perfect as ever!"
        show maria at left
        w "Waaahh... you know Maria, you looked very beautiful running into the room with that fire extinguisher."
        show wah happy nostache at right
        w "I think I am in love with you. Wahnna be my girlfriend?"
        play music "sad.mp3"
        show maria happy at left
        m "Oh my!! Of course! Yes, I love you too!"
        show ending sad
        "Somehow... I feel empty inside."
        "Sad End."
        return
### SCENE 3 (B)

    label scene3_b:
        play music "pinball.mp3"
        "(The next day, afterschool...)"

        scene classroom
        #with fade

        e "This place looks exactly how I thought it would..."
        #scene wah club
        show wah
        w "WAHH?? Waht are you doing here?"
        e "I wahnna join the WAH club"
        w "Wahhh! You made the right choice! I see you are a man of culture"
        e "Uh yeah... so what exactly do you do here?"
        w "All things WAH, of course!"
        e "And what exactly does that mean??"
        w "Well, I'll give you some options... would you rather WAH, or wahhh?"
        menu:
            "WAH":
                jump choice3_WAH
            "wahhh":
                jump choice3_wah
        label choice3_WAH:
            show wah happy
            w "Okay! After me, scream WAH!"
            w "WAH!"
            e "...WAH!"
            jump choice3_done
        label choice3_wah:
            show wah happy
            w "Okay! After me, whisper softly...wahhh"
            e "...wahhh"
            jump choice3_done
        label choice3_done:
        show wah
        w "See? Wahsn't that fun?"
        e "Not really... can't we do anything else?"
        w "We could talk"
        e "About what?"
        w "Why did you want to join my club?"
        menu:
            "Lie":
                jump choice4_lie
            "Tell him the truth":
                jump choice4_tru
        label choice4_lie: #### END 2

            stop music fadeout 1
            play music "careless whisper.mp3"



            e "Uhh... I am very passionate about the WAH... ya know?"
            show wah happy
            w "Wahhh, really?"
            e "...yes"
            show wah
            w "That makes me so happy... no one ever appreciates a good wahhh."
            e "I'm sorry to hear that."
            w "But you do! And you were willing to wahhh with me."
            w "Wahhh... you're not like the others, you know."
            e "Uhhh, what do you mean??"
            w "Wahhh :3"
            e "Uhmm... I think I should go."
            w "I'm in love with you."
            e "owo ???"
            w "Wahnna be my girlfriend?"
            "This is bad... he's supposed to say this to Maria!"
            "But then again... does Maria even deserve him?"
            "And he IS pretty dreamy..."
            menu:
                "Yes":
                    jump choice_love
                "No":
                    jump choice_reject
            label choice_love: ### END 2 A)
                e "...Okay."
                e "I think I love you too."
                show wah happy
                w "Wahhh! You make me so happy."
                m "YOU TRAITOR!"
                show wah at left
                show maria sad at right
                e "Whoa! When did you get here!"
                m "I was spying to make sure you were doing your job, and obviously you weren't!"
                m "I can't believe you did this!"
                m "I should have never trusted you!!"
                w "Wahhhh?"
                e "lol oops."
                show end 2a
                "End."
                return
            label choice_reject: #### END 2 B)
                e "No... I'm sorry."
                show wah sad
                w "Waht?? Why not?"
                e "There's someone else who already likes you."
                e "Plus... I don't really appreciate the wah."
                w "So... you lie??"
                e "Yep... sorry dood."
                w "Wahhh."
                m "BUT I DO!!"
                show wah at left
                show maria at right
                e "How'd you get here?"
                m "I was spying to make sure you were doing your job!"
                e "You could've done all this yourself you know..."
                m "Forget about this loser Waluigi... I love you and the wah more than anything!"
                show wah happy at left
                w "Wahhh?? Then you can be my girlfriend."
                play music "sad.mp3"
                show maria happy at right
                m "Yess!!!"
                show ending sad
                "Sad End."
                return
        label choice4_tru: ### END 3 (WORST)
        show wah
        e "If you want the truth, I'm only here because I'm helping out a friend."
        e "Actually wait, she's not even my friend."
        w "Wahhh??"
        e "I won't say who, but there's this girl who wanted to get to know you better."
        e "I mean she could've just done this HERSELF but for the sake of this lazy plot, I'm doing it for her."
        e "So yeah, I'm just here to get to know you better, and then give the info to her."
        e "So there ya go."
        w "Wait..."
        w "So you're telling me..."
        w "This whole time..."
        show wah mad
        w "YOU DIDN'T ACTUALLY WANT TO JOIN THE WAH CLUB???"
        e "What."
        w "No one appreciates a good wah! I cannot believe this!"
        w "I hate you! And you're stoopid friend too!"
        e "Oh my god, she's not my friend!"
        play music "sad.mp3"
        scene shook
        "Worst End."











    # This ends the game.

    return
