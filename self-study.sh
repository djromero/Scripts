#!/bin/sh

pause=0.2

voices=( "Alex" "Samantha" )
len_voices=${#voices[*]}

intro()
{
    say three
    sleep $pause
    say two
    sleep $pause
    say one
    sleep $pause
    say go
    sleep $pause
    clear
}

say_words()
{
    declare -a words=("${!1}")
    len=${#words[*]}
    typeset -i idx=0
    typeset -i voice_idx=0
    while [[ $idx -lt $len ]] 
    do
        voice_idx=$(( RANDOM % $len_voices ))
        word=${words[$idx]}
        let idx=$idx+1
        say -v ${voices[$voice_idx]} $word
        read x
        clear
        echo
        echo
        echo
        echo
        echo '          ' $word
        echo
        echo
        echo
        echo
        read x
        sleep $pause
    done
}

#intro
read x

verbs=( "I'm working" "We're working" "I'm listening" "We're painting"  "I'm eating" "We're reading and singing" "I'm working" "We're watching" )
say_words verbs[@]

grammar=( "Where's Paula?" "She's in the bathroom" "What's she doing?" "She's washing her hands" )
say_words grammar[@]

days=( "On Monday we paint" "On Tuesday we study" "Wednesday" "Thursday" "On Friday we work" "Saturday" "On Sunday we play" )
say_words days[@]

subjects=( "P.E." "Maths" "Reading" "Writing" "Art" "English" "I like P.E." "I don't like Maths" "Do you like Art? Yes I do." )
say_words subjects[@]

vocab2=( "rat" "bed" "fish" "frog" "sun" "drum" "clock" "ship" "jet" "lamp" )
say_words vocab2[@]

music=( "flute" "trumpet" "cello" "drum" "violin" "tambourine" "piano" "guitar" "saxophone" "double bass" )
say_words music[@]

vocab=( "art room" "assembly hall" "canteen" "classroom" "computer lab" "gym" "library" "playground" )
say_words vocab[@]

