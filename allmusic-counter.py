# -*- coding: utf-8 -*-
# 
# Count artists/songs to know which ones has been favorited more often.
#

# copy here the text from allmusic page
allmusic = """
Stephen Thomas Erlewine
Jarvis Cocker – Further Complications
Lily Allen – It’s Not Me, It’s You
Brad Paisley – American Saturday Night
Julian Casblancas – Phrazes for the Young
La Roux – La Roux
The Black Crowes – Before the Frost/Until the Freeze
Shakira – She Wolf
Weezer – Raditude
Lady Gaga – The Fame Monster
Sonic Youth – The Eternal
Them Crooked Vultures – Them Crooked Vultures
Norah Jones – The Fall
Madness – The Liberty of Norton Folgate
Arctic Monkeys – Humbug
Manic Street Preachers – Journal for Plague Lovers
The Fiery Furnaces – I’m Going Away
Bob Dylan – Together Through Life
Dan Auberach – Keep It Hid
Neko Case – Middle Cyclone
Coconut Records – Davy

The Black Crowes – “Good Morning Captain”
Kelly Clarkson – “I Do Not Hook Up”
Weezer – “If Youâ€™re Wondering If I Want You To (I Want You To)”
Lily Allen – “Not Fair”
Britney Spears – “3″
Art Brut – “Slap Dash for No Cash”
Lady Gaga – “Poker Face”
Lady Gaga – “Bad Romance”
George Strait – “Twang”
Dan Auberach – “My Mistake”

John Bush
Animal Collective – Merriweather Post Pavilion
The xx – xx
The Dirty Projectors – Bitte Orca
Anti-Pop Consortium – Fluorescent Black
Grizzly Bear – Veckatimest
The Flaming Lips – Embryonic
Neon Indian – Psychic Chasms
Jay Reatard – Watch Me Fall
St. Vincent – Actor
The-Dream – Love vs Money
DÃ¢m-Funk – Toeachizown
Bill Callahan – Sometimes I Wish We Were an Eagle
Brad Paisley – American Saturday Night
The Fiery Furnaces – I’m Going Away
tUnE-yArDs – Bird-Brains
A Place to Bury Strangers – Exploding Head
The Very Best – Warm Heart of Africa
YACHT – See Mystery Lights
Wale – Attention Deficit

The xx – “Crystalised”
Jack PeÃ±ate – “Pull My Heart Away [Jamie xx Remix]”
Washed Out – “Feel It All Around”
Black Moth Super Rainbow – “Born on a Day the Sun Didn’t Rise”
Bill Callahan – “Eid Ma Clack Shaw”
Jay Reatard – “It Ain’t Gonna Save Me”
The Dead Weather – “Hang You from the Heavens”
Camera Obscura – “French Navy”
The Pains of Being Pure at Heart – “Come Saturday”
Neon Indian – “Terminally Chill”
Phoenix – “Fences [Friendly Fires Remix]”
Discovery – “Orange Shirt”
Lupe Fiasco – “The National Anthem”
The-Dream – “Walkin’ on the Moon”
Wale f/ Pharrell – “Let It Loose”
YACHT – “Ring the Bell”
Grizzly Bear – “Two Weeks”
St. Vincent – “The Strangers”
Flight of the Conchords – “We’re Both in Love with a Sexy Lady”
Beck – “Harry Partch”

Heather Phares
Bibio – Ambivalence Avenue
Tyondai Braxton – Central Market
Cold Cave – Love Comes Close
Fever Ray – Fever Ray
The Fiery Furnaces – I’m Going Away
The Flaming Lips – Embryonic
Future of the Left – Travels With Myself and Another
Fuck Buttons – Tarot Sport
Grizzly Bear – Veckatimest
PJ Harvey – A Woman a Man Walked By
La Roux – La Roux
Micachu – Jewellery
Mount Eerie – Wind’s Poem
Major Lazer – Guns Don’t Kill People, Lazers Do
Real Estate – Real Estate
Sonic Youth – The Eternal
St. Vincent – Actor
Talk Normal – Sugarland
Wildbirds & Peacedrums – The Snake
The xx – xx
The Yeah Yeah Yeahs – It’s Blitz!

Jarvis Cocker – “Angela”
Cold Cave – “Life Magazine”
Dead Weather – “Treat Me Like Your Mother”
Fever Ray – “If I Had a Heart”
Fiery Furnaces – “The End is Near”
Grizzly Bear – “Two Weeks”
PJ Harvey – “Black Hearted Love”
La Roux – “Quicksand”
Lady Gaga – “Bad Romance”
Major Lazer – “Keep it Getting Louder”
Micachu – “Golden Phone”
Britney Spears – “3″
Shakira – “She Wolf”
St. Vincent – “Actor Out of Work” (YouTube)
Talk Normal – “In a Strangeland” (YouTube)
Wildbirds & Peacedrums – “My Heart”
The xx – “Basic Space”
Yeah Yeah Yeahs – “Heads Will Roll”

Tim Sendra
Afternoon Naps – Parade
Bricolage – Bricolage
Burning Hearts – Aboa Sleeping
Camera Obscura – My Maudlin Career
City Center – City Center
The Clientele – Bonfires on the Heath
Cola Jet Set – Guitarras y Tambores
The CrÃªpes – So What Else?
Discovery – LP
Drake – So Far Gone
Fitness Forever – Personal Train
Get Back Guinozzi! – Carpet Madness
Girls – Album
jj – jj NÂº 2
La Roux – La Roux
Lake Heartbeat – Trust in Numbers
Sondre Lerche – Heartbeat Radio
The Pastels/Tenniscoats – Two Sunsets
Summer Cats – Songs for Tuesdays
The xx – xx

Bounce Camp – “Good Beat”
Kelly Clarkson – “I Do Not Hook Up”
Drake – “Best I Ever Had”
Internet Forever – “Break Bones”
Lake Heartbeat – “Mystery”
La Roux – “Bulletproof”
Little Boots – “Stuck on Repeat”
Lucky Soul – “Whoa Billy”
The Magic Kids – “Hey Boy”
Washed Out – “Feel It All Around”

Matt Collar
Annie – Don’t Stop
Dan Auerbach – Keep It Hid
Brendan Benson – My Old, Familiar Friend
The Black Crowes – Before the Frost/Until the Freeze
Jarvis Cocker – Further Complications
Dinosaur Jr. – Farm
Frankmusik – Complete Me
Franz Ferdinand – Tonight
Guggenheim Grotto – Happy the Man
Richard Hawley – Truelove’s Gutter
La Roux – La Roux
Maxwell – BLACKsummers’night
John Mayer – Battle Studies
Paramore – Brand New Eyes
Phoenix – Wolfgang Amadeus Phoenix
Shakira – She Wolf
St. Vincent – Actor
Temper Trap – Conditions
Weezer – Raditude
Patrick Wolf – The Bachelor

Greg Heaney
The Flaming Lips – Embryonic
Coalesce – Ox
Felt – Felt 3: Tribute to Rosie Perez
Isis – Wavering Radiant
Animal Collective – Merriweather Post Pavilion
Method Man & Redman – Blackout, Vol. 2
Russian Circles – Geneva
Goblin Cock – Come with Me If You Want to Live
Baroness – Blue Record
Muse – The Resistance
I Come to Shanghai – I Come to Shanghai
The Decemberists – The Hazards of Love
Converge – Axe to Fall
Mos Def – The Ecstatic
The Thermals – Now We Can See
Wavves – Wavvves
Grizzly Bear – Veckatimest
Pelican – What We All Come to Need
MF Doom – Born Like This
Thee Oh Sees – Help

Lil Wayne – “I’m Goin In”
Coalesce – “In My Wake, for My Own”
Snoop Dogg – “Upside Down”
Electric Six – “Body Shot”
Eagle Twin – “Carry On, King of Carrion”
Lightning Bolt – “Colossus”
I Come to Shanghai – “Your Lazy Eye”
The Bird and the Bee – “Dance Song”
The Flaming Lips – “Worm Mountain”
Goblin Cock – “We Got a Bleeder”
Rick Ross – “Maybach Music”
White Denim – “Say What You Want”
Pelican – “Ephemeral”
The Flaming Lips w/ Stardeath and White Dwarfs – “Borderline”
Gucci Mane – “Stupid Wild”
Tyvek – “Michael Caine”
The Thermals – “Now We Can See”
Isis – “20 Minutes/40 Years”

David Jeffries
Alborosie – Escape from Babylon
Buju Banton – Rasta Got Soul
Clipse – Til the Casket Drops
Leonard Cohen – Live in London
DJ Quik & Kurupt – BlaQKout
Kid Cudi – Man on the Moon: The End of Day
Lady Saw – Extra Raw: The Best of Lady Saw
Major Lazer – Guns Don’t Kill People…Lazers Do
Ziggy Marley – Family Time
Mavado – Mr. Brooks…A Better Tomorrow
Freddie McGregor – Mr. McGregor
Method Man & Redman – Blackout! Vol. 2
Patton Oswalt – My Weakness Is Strong
Dudley Perkins – Holy Smokes
Raekwon – Only Built 4 Cuban Linx, Pt. 2
Tarrus Riley – Contagious
Winston Riley – Quintessential Techniques: Reggae Anthology
Slaughterhouse – Slaughterhouse
Tiny Masters of Today – Skeletons
Version Big-Fi – Crux Collide Hybridize

Thom Jurek
Tony Allen & Jimi Tenor – Inspiration Information, Vol. 4
James Blackshaw – The Glass Bead Game
Ran Blake – Driftwoods
DÃ¢m-Funk – Toeachizown
Betty Davis – Is It Love or Desire
Blut Aus Nord – Memoria Vetusta II/Dialogue with the Stars
Ariana Delawari – Lion of Panjshir
Ben Frost – By the Throat
Jan Garbarek – Dresden in Concert
Joe Henry – Blood from Stars
Kris Kristofferson – Closer to the Bone
Buddy & Julie Miller – Written in Chalk
Georgia Anne Muldrow – Umsindo
My Dying Bride – For Lies I Sire
Nomo – Invisible Cities
Kelly Joe Phelps – Western Bell
Tom Russell – Blood and Candle Smoke
Sa-Ra – Nuclear Evolution: The Age of Love
Peter Walker – Long Lost Tapes, 1970
John Zorn – O’o

Andy Kellman
Audision – Surface to Surface
Diego Bernal – For Corners
Clipse – Til the Casket Drops
DÃ¢m-Funk – Toeachizown
DJ Quik & Kurupt – BlaQKout
The-Dream – Love vs Money
Keri Hilson – In a Perfect World…
Shafiq Husayn – Shafiq En’ A-Free-Ka
J Dilla – Jay Stay Paid
King Midas Sound – Waiting for You
Maxwell – BLACKsummers’night
Mos Def – The Ecstatic
Georgia Anne Muldrow – Umsindo
Omar-S – Fabric 45
PPP – Abundance
Redshape – The Dance Paradox
Sa-Ra – Nuclear Evolution: The Age of Love
2562 – Unbalance
Moritz von Oswald Trio – Vertical Ascent
The xx – xx

Black Jazz Consortium – “Mind in Flight”
Build an Ark – “Celebrate”
Calibre – “Stolen Shadow”
Dorian Concept – “Trilingual Dance Sexperience” (YouTube)
Walter Jones – “Living Without Your Love”
K. Michelle – “Fakin’ It”
Kode9 – “Black Sun”
Ryan Leslie – “You’re Not My Girl”
Little Dragon – “Fortune”
Lone – “Joyreel”
Millie & Andrea – “Temper Tantrum”
Moody – “Freeki Mutha F cker”
Mount Kimbie – “Sketch on Glass”
Joy Orbison – “Hyph Mngo” (YouTube)
Portishead – “Chase the Tear”
Rebolledo – “Guerrero”
Sade – “Soldier of Love”
Kuba Sojka – “Message from Earth”
2000F & J Kamata – “You Don’t Know What Love Is” (YouTube)
Zomby – “Godzilla”

Andrew Leahey
Miranda Lambert – Revolution
Neko Case – Middle Cyclone
Phoenix – Wolfgang Amadeus Phoenix
Dan Auerbach – Keep It Hid
Tom Petty & the Heartbreakers – The Live Anthology
Miranda Lee Richards – Light of X
Muse – The Resistance
Paramore – Brand New Eyes
Lissie – Why You Runnin’
Great Lake Swimmers – Lost Channels
Le Loup – Family
The Swell Season – Strict Joy
Exebelle & the Rusted Cavalcade – The Antipoison Creek Sessions
Speck Mountain – Some Sweet Relief
Ben Kweller – Changing Horses
Ingrid Michaelson – Everybody
The Low Anthem – Oh My God, Charlie Darwin
The Skygreen Leopards – Gorgeous Johnny
Alvin Band – Mantis Preying

Arctic Monkeys – “Cornerstone”
Miranda Lambert – “Airstream”
The Everyday Visuals – “Daydream Ghosts”
Muse – “Guiding Light”
Robert Francis – “Junebug”
Great Lake Swimmers – “Everything Is Moving So Fast”
Dan Auerbach – “When the Night Comes”
Sleigh Bells – “Ring Ring”
Maria Taylor – “Cartoons and Forever Plans”
Exebelle & the Rusted Cavalcade – “What If We Fell”
Emmy the Great – “We Almost Had a Baby”
U2 – “No Line on the Horizon”
A Fine Frenzy – “Electric Twist
Paramore – “Careful”
Elvis Perkins – “How’s Forever Been Baby”
Grizzly Bear – “Two Weeks”
Keith Urban – “‘Til Summer Comes Around”

Jason Lymangrover
Bibio – Vignetting the Compost
Clark – Totems Flare
Crocodiles – Summer of Hate
DÃ¤lek – Gutter Tactics
Double Dagger – More
The Flaming Lips – Embryonic
Girls – Album
Health – Get Color
Japandroids – Post-Nothing
James Pants – Seven Seals
Kid Cudi – Man on the Moon: The End of Day
Lotus Plaza – The Floodlight Collective
Lovvers – OCD Go Go Girls
Mos Def – The Ecstatic
Odd Nosdam – T.I.M.E. Soundtrack
Marked Men – Ghosts
Jay Reatard – Watch Me Fall
Tiny Masters of Today – Skeletons
Wavves – Wavvves
White Denim – Fits

Art Brut – “DC Comics and Chocolate Milkshake”
Black Lips – “Starting Over”
BLK JKS – “Lakeside”
Box Elders – “Stay”
Camp Lo – “2 Dope Boyz”
Chain & the Gang – “Deathbed Confession”
Christmas Island – “Bed Island”
Crystal Antlers – “Glacier”
Goblin Cock – “We Got a Bleeder”
Jay-Z – “D.O.A. (Death of Autotune)”
Lullabye Arkestra – “Fog Machine”
Mi Ami – “New Guitar”
Micachu & the Shapes – “Calculator”
Mika Miko – “Turkey Sandwich”
Pissed Jeans – “False Jesii, Pt. 2″
Kurt Vile – “Freak Train”
Sonic Youth – “Antenna”
Titus Andronicus – “Titus Andronicus”
Tyvek – “Stop Start”
Warlocks – “The Midnight Sun”

James Christopher Monger
Florence and the Machine – Lungs
Hot Leg – Red Light Fever
Eugene McGuinness – Eugene McGuinness
A.C. Newman – Get Guilty
The Clientele – Bonfires on the Heath
The Duckworth Lewis Method – The Duckworth Lewis Method
Matt Jones – The Black Path
Muse – The Resistance
Neko Case – Middle Cyclone
Bonnie “Prince” Billy – Beware
Horse’s Ha – Of the Cathmawr Yards
TÃ½r – By the Light of the Northern Star
Avett Brothers – I and Love and You
The Low Anthem – Oh My God, Charlie Darwin
Hidden Cameras – Origin:Orphan
A.A. Bondy – When the Devil’s Loose
Liam McKahey & the Bodies – Lonely Road
The Hard Lessons – Arms Forest
Ensiferum – From Afar
Huun-Huur-Tu/Carmen Rizzo – Eternal
Wild Light – “California on My Mind”
Black Joe Lewis & the Honeybears – “Bitch, I Love You”
Big Pink – “Dominoes”
Depeche Mode – “Wrong”
Edward Sharp and the Magnetic Zeroes – “40 Day Dream”
Future of the Left – “The House That Hope Built”
Micachu – “Golden Phone”
Fanfarlo – “I’m a Pilot”
The Delta Spirit – “People C’mon”
Jeremy Enigk – “Life’s Too Short”
Royksopp – “The Girl and the Robot”
Espers – “Caroline”
The Gourds – “Shreveport”
Wild Beasts – “All the King’s Men”
Broken Records – “Nearly Home”
Andrew Bird – “Oh No”
Phoenix – “1901″
Animal Collective – “My Girls”
The Very Best – “Yalira”
Andy Prieboy – “Hearty Drinking Men”

Sean Westergaard
Fred Anderson – 21st Century Chase: 80th Birthday Bash, Live at the Velvet Lounge
The Beatles – The Beatles: Mono Box Set
Sir Richard Bishop – Freak of Araby
James Carter/John Medeski – Heaven on Earth
Bo Diddley – Ride On: The Chess Masters, Vol. 3 – 1960-1961
Marc Ducret – Sens de la Marche
Mike Keneally – Scambot 1
King Crimson – Red 40th Anniversary Edition
Korekyojinn – Swan Dive
Wayne Krantz – Krantz Carlock Lefebvre
Medeski Martin & Wood – Radiolarians: The Evolutionary Set
Miriodor – Avanti!
Ben Perowsky Quartet – Esopus Opus
Sun Ra & His Arkestra – The Antique Blacks
Omar Rodriguez-Lopez – Old Money
Sax Ruins – Yawiquo
Wadada Leo Smith – Spiritual Dimensions
Imahori Tsuneo/Yoshida Tatsuya – Dots
John Zorn – O’o
John Zorn – Film Works, Vol. 23: El General
"""

import re
artists = {}
songs = {}
songsby = {}
sep=re.compile("(?P<artist>[^–]+) – (?P<song>.+)")
for line in allmusic.split("\n"):
    if line == "" or not "–" in line:
        continue
    m = sep.match(line)
    if m:
        if not m.group("artist") in artists:
            artists[m.group("artist")] = 0
        artists[m.group("artist")] += 1
        if not m.group("song") in songs:
            songsby[m.group("song")] = m.group("artist")
            songs[m.group("song")] = 0
        songs[m.group("song")] += 1

print "Bands"
print "-----"
for (artist, hits) in sorted(artists.items(), key=lambda x:x[1], reverse=True):
    if hits <= 2:
        continue
    print "* %s (%d)" % (artist, hits)

print "Songs"
print "-----"
for (song, hits) in sorted(songs.items(), key=lambda x:x[1], reverse=True):
    if hits <= 2:
        continue
    print "* %s by %s (%d)" % (song, songsby[song], hits)
