#I will be creating a function for my project, which is to make a 2020 random playlist generator. The function I will be using is "genre," which will define the types of songs for my generator. I intend for the genre function to be defined by music attributes, such as Pop, Rock, Hip Hop, R&B, ect. Its argument would be "songs" since I will have specific lists of songs that categorize each genre. Likely, the return value would be "songs".

#Below are a few lists containing songs that categorize each genre for my generator. More will be filled out at a later time.
pop = ["Therefore I Am by Billie Eilish", "Stupid Love by Lady Gaga", "Momentary Bliss by Gorillaz", "After Hours by The Weeknd", "foreover by Charli XCX", "Rain On Me by Lady Gaga & Ariana Grande", "Physical by Dua Lipa", "At The Door by The Strokes", "Lucid by Rina Sawayama", "Midnight Sky by Miley Cyrus", "Dynamite by BTS", "Say So by Doja Cat", "Daises by Katy Perry", "Daylight by Joji & Diplo", "Prisoner by Miley Cyrus ft. Dua Lipa", "Break My Heart by Dua Lipa", "Spotlight by Jessie Ware", "Smile by Katy Perry", "Let's Be Friends by Carly Rae Jepsen", "Levitating by Dua Lipa", "Wonder by Shawn Mendes", "Love Me Land by Zara Larsson", "You should be sad by Halsey", "Take Yourself Home by Troye Sivan", "All The Things She Said by Poppy", "Get your Wish by Porter Robinson", "People, I've been sad by Christine and the Queens", "Gentleman by Dorian Electra", "Rare by Selena Gomez", "Caution by The Killers", "Give Great Thanks by Dorian Electra", "Oh Yeah! by Green Day", "I Love Me by Demi Lovato", "Time Flies by Tori Kelly", "I'm Ready by Sam Smith & Demi Lovato", "Nobody's Love by Maroon 5", "911 by Lady Gaga", "Love In My Pocket by Rich Brian", "Monster by Shawn Mendes & Justin Bieber" "Only the Young by Taylor Swift", "The Man by Taylor Swift", "Fever by Dua Lipa & Angèle", "Say Something by Kylie Minogue", "Ooh La La by Jessie Ware", "Bang! by AJR", "My Oh My by Camila Cabello", "Save A Kiss by Jessie Ware", "Easy by Troye Sivan", "Kings & Queens by Ava Max", "In Your Eyes by The Weeknd", "Lifetime by Romy", "Exist For Love by AURORA", "Bloody Valentine by Machine Gun Kelly", "Bikini Porn by Tove Lo", "Feel Me by Selena Gomez", "Malibu by Kim Petras", "The Other Side by SZA & Justin Timberlake", "What A Man Gotta Do by Jonas Brothers", "Wild Nothing by Foyer", "React by The Pussycat Dolls", "Birthday by Anne-Marie", "Who's Laughing Now by Ava Max", "Savage Love (Laxed- Siren Beat)[BTS Remix] by Jawsh 685, Jason Derulo, & BTS", "Feelings by Lauv", "Diamonds by Sam Smith", "Mad at Disney by salem ilese", "Lose You to Love Me by Selena Gomez", "Heather by Conan Gray", "positions by Ariana Grande", "Watermelon Sugar by Harry Styles", "Blueberry Eyes by MAX ft. SUGA", "Experience by Victoria Monét & Khalid", "Before You Go by Lewis Capaldi", "Fly Away by Tones and I", "My Oasis by Sam Smith ft. Burna Boy", "you broke me first by Tate McRae", "Know Your Worth by Khalid & Disclosure", "just a boy by Alaina Castillo", "Don't Take Me Home by Tori Kelly"]

kpop = ["Black Swan by BTS", "Ice Cream by BLACKPINK & Selena Gomez", "Stay Tonight by CHUNG HA", "pporappippam by Sunmi", "Naughty by Red Velvet- IRENE & SEULGI", "Eight by IU ft. SUGA from BTS", "Yesterday by YUKIKA", "THE BADDEST by K/DA", "DUMDi DUMDi by (G)I-DLE", "Helicopter by CLC", "What You Waiting For by SOMI", "DESSERT by HYO", "The First Step: Chapter One by TREASURE", "When We Disco by J.Y. Park & Sunmi", "Happy by TAEYEON", "2 KIDS by Taemin", "100 by SuperM", "WANNA BE MYSELF by MAMAMOO", "Who Dis? By SECRET NUMBER", "THANXX by ATEEZ", "Unknown Art Pop 2.1 by OnlyOneOf", "God's Menu by Stray Kids", "Yaya (Me Time) by Yubin", "LAST PIECE by GOT7", "Tiger Inside by SuperM", "Kick It by NCT 127", "HOME;RUN by SEVENTEEN" "J.us.T by Eyedi", "ASSA by Cignature", "I'M THE TREND by (G)I-DLE", "Nun Nu Nan Na by Cignature", "Do or Die by AleXa", "LOVELY by Minzy", "Bird by Kim Nam Joo", "La Luna by HA:TFELT", "Snowman by Brown Eyes Girls", "Paradise by SIYEON", "Take Me Now by LUNA", "It Hurts and Hurts by LUNA", "Spring by MCND", "Children by BVNDIT", "Hug Me Silently by Hyolyn & Crucial Star", "Let's Love (with Spoonz) by NU'EST", "A.I. Trooper by AleXa", "Can't You See Me? by TXT", "Still Standing by YESUNG & SURAN", "Everyone by ONF", "Road to Kingdom by ONEUS, TOO, & ONF", "In the Summer by SSAK3", "Beach Again by SSAK3", "Dreaming by KYUHYUN", "Mmmh by KAI", "Turn Back Time by WayV", "LA DI DA by EVERGLOW", "I CAN'T STOP ME by TWICE", "DUN DUN by EVERGLOW", "DAECHWITA by Agust D", "ON BY BTS", "CANDY by BAEKHYUN", "How You Like That by BLACKPINK", "Dumhdurum by Apink", "Maria by Hwasa", "Puma by TXT", "Back Door by Stray Kids", "Oh my god by (G)I-DLE", "Lovesick Girls by BLACKPINK", "Life Goes On by BTS", "You by Dynamicduo & CHEN", "Happy Day by H&D", "Lover by Kwon Jin Ah", "Unfamiliar by H&D", "Flower by Park Ji Yoon", "Something's Wrong by Kwon Jin Ah", "Refresh by ZICO & KANG DANIEL", "No Good Girl by Minseo", "Very Good by Pentagon", "Shine + Spring Snow by Pentagon", "Spit it out by Solar", "FIESTA by IZ*ONE", "WANNABE by ITZY", "Secret Story of the Swan by IZ*ONE", "INCEPTION by ATEEZ", "NOT SHY by ITZY", "NOT BY THE MOON by GOT7", "Blue Hour by TXT", "OPEN MIND by WONHO", "Boom by LAY", "Make A Wish (Birthday Song) by NCT U", "Love Killa by MONSTA X"]

r&b = ["Distance by Yebba", "Waiting For by rum.gold ft. Jamila Woods", "For Us by dvsn", "Heart-Shaped Box by Amber Mark", "Veg Out (Wasting Thyme) by Masego", "Plastic Plants by Mahalia", "SBCNCSLY by Black Cofee & Sabrina Claudio", "Clutch by Col3trane ft. Kiana Ledé", "My House by Elah Hale", "Forgive Me by Chloe x Halle", "Quarantine Queen by Sinead Harnett", "These Days by Tems", "DYING 4 YOUR LOVE by Snoh Aalegra", "Mad At Me. by Kiana Ledé", "It's a Moot Point by Melanie Faye", "Bittersweet by Lianne La Havas", "Good & Plenty by Alex Isley & Masego & Jack Dine", "Make Me Feel by Skip Marley ft. Ari Lennox", "Summer 2020 by Jhené Aiko", "Brandy by Full Crate ft. Kyle Dion", "So Done by Alicia Keys ft. Khalid", "Jaguar by Victoria Monét", "Only One by Gallant", "Make the Most by Lonr. ft. H.E.R.", "Bedtime Story by RINI", "Stickin' by Sinead Harnett ft. Masego & VanJess", "By Any Means by Jorja Smith", "Woman by Nao ft. Lianne La Havas", "So Much More by Xavier Omär", "More Than Enough by Alina Baraz", "Beautiful Lies (Cold) by Lol Zouaï", "Icy by Pink Sweat$", "Come Over by Jorja Smith ft. Popcaan", "Silver Tongue Devil by Masego & Shenseea", "Not Another Love Song by Ella Mai", "RUN by KWAYE", "damage by H.E.R.", "Temptation by Tiwa Savage ft. Sam Smith", "Cayendo by Frank Ocean", "Hit Different by SZA", "Black Parade by Beyoncé", "Rooted by Ciara ft. Ester Dean", "Pick Up Your Feelings by Jazmine Sullivan", "Mystery Lady by Masego & Don Toliver", "Pretend by Queen Naija", "Perfect Time by Luh Kel", "High & Dry by VanJess", "No Tomorrow, Pt.2 by Brandy ft. Ty Dolla $ign", "Always Foreover by Bryson Tiller", "Bad Habits by Usher", "safety net by Ariana Grande ft. Ty Dolla $ign", "Stuck On You by Giveon", "Crowns and Diamonds by Mario", "Do You Well By Omarion", "See What You've Done by Mary J. Blige", "I Wish by DaniLeigh ft. Ty Dolla $ign", "On and On by THEY.", "Devotion by Tone Stith", "Do It by Chloe x Halle", "Superpower by KIRBY & D Smoke", "Lovesick by RAY BLK", "By Yourself by Ty Dolla $ign ft. Mustard & Jhené Aiko", "You Ain't Worth It by Melii & 6LACK", "Pick A Side by Raiche", "Ooh Laa by John Legend", "You Save Me by Alicia Keys ft. Snoh Aalegra", "Borderline by Brandy", "Love Song by Vivian Green", "Chocolate Pomegranate by Ari Lennox", "Do It by Toni Braxton", "Sweeter by Leon Bridges ft. Terrace Martin", "Wake Up Love by Teyana Taylor ft. IMAN"]

hip-hop = ["Wash Us in the Blood by Kanye West", "WAP by Cardi B & Megan Thee Stallion", "@ MEH by Playboi Carti", "Toosie Slide by Drake", "Bald! by JPEGMAFIA", "GOOBA by 6ix9ine", "THE SCOTTS by Travis Scott & Kid Cudi", "The Adventures of Moon Man and Slim Shady by Eminem & Kid Cudi", "Franchise by Travis Scott", "iPhone by Rico Nasty", "Pig Feet by Terrace Martin & Denzel Curry", "Laugh Now Cry Later by Drake", "Sasuke by Lil Uzi Vert", "Leader of the Delinquents by Kid Cudi", "Holiday by Lil Nas X", "Life Is Good by Future", "The Plan by Travis Scott", "Covered in Money! by JPEGMAFIA", "Ego Death by Ty Dolla $ign", "That Way by Lil Uzi Vert", "N.S.T. by BROCKHAMPTON", "Ooh LA LA by Run The Jewels", "Lewis Street by J. Cole", "Say the Name by clipping.", "Lockdown by Anderson.Paak", "Righteous by Juice WRLD", "The Bigger Pciture by Lil Baby", "Snow On Tha Bluff by J. Cole", "Fall Slowly by Joyner Lucas ft. Ashanti", "Whole World by Earl Sweatshirt", "Darkness by Eminem", "SUGAR (Remix) by BROCKHAMPTON", "Nah Nah Nah (Remix) by Kanye West", "Don't Stop by Megan Thee Stallion", "Chicago Freestyle by Drake", "Sum Bout U by 645AR", "Smile by Juice WRLD & The Weeknd", "Savage Remix by Megan Thee Stallion", "Song 33 by Noname", "Yikes by Nicki Minaj", "death bed by Powfu", "Popstar by DJ Khaled ft. Drake", "4 Da Trap by 645AR", "Godzilla by Eminem", "Boss Bitch by Doja Cat", "Turks by Nav & Gunna", "Greece by DJ Khaled", "Will by Joyner Lucas", "Burn The Hoods by Ski Mask The Slump God", "Over Your Head by Future & Lil Uzi Vert", "OHFR? by Rico Nasty", "Rodeo (Remix) by Lil Nas X", "Oprah's Bank Account by Lil Yachty & DaBaby", "When To Say When by Drake", "nhs by slowthai", "Violence by Yung Lean", "ENEMY by slowthai", "Gifted by Cordae", "keep your distance by Ameer Vann", "Compensating by Aminé", "Entrepeneur by Pharell Williams ft. Jay-Z", "Patek by Future & Lil Uzi Vert", "hooligan / sons & critics by Baby Keem", "Blueberry Faygo by Lil Mosey", "Shimmy by Aminé", "All Week by Rod Wave", "Finally Rich by Lil Eazzyy", "Cancelled by Larray", "Lets Link by WhoHeem ft. Tyga & Lil Mosey", "MAD by 2KBABY", "Revenge by $NOT", "The Parables by Cordae", "Loser by Rico Nasty ft. Trippie Redd", "For The Night by Pop Smoke ft. Lil Baby & DaBaby", "Gucci Peacoat by DaBaby", "Wolves by Big Sean ft. Post Malone", "Gorgeous by SAINt JHN", "I Got You by Trippie Redd", "Runnin by 21 Savage & Metro Boomin"]

#These are placeholders of lists I will fill out at a later time.
rock = [""]

latin = [""]

dancehall = [""]

alternative = [""]

edm = [""]

country = [""]


def create_genre(songs):
    genre = ""
    song_number = random.randint(0, 80)
#Shown above is my attempt at making sure my generator would produce a random output from the list above. The numbers in the parentheses refer to the list's start and end so that the range would randomly select songs between those points. "Therefore I Am by Billie Eilish" is 0, which is the starting point while "Don't Take Me Home by Tori Kelly" is the ending point at 80.
    for item in range(0, song_number):
        song_to_pop = random.randint(0, len(songs) - 1)
        genre += songs.pop(song_to_pop) + " "
#The for loop shown above is using the pop method to keep the list from iterating duplicates of songs so that the generator would not continuously show the same songs repeatedly. Hopefully, each song would be able to be seen at least once.
    return genre

print create_genre(pop)
print(*pop, sep = "\n")
#The print statement above is to ensure that each song from the "pop" list would print on a new line instead of being separated by commas and spaces. This would likely be more reminiscent of a genre playlist.

def create_genre(songs):
    genre = ""
    song_number = random.randint(0, 89)
    for item in range(0, song_number):
        song_to_pop = random.randint(0, len(songs) - 1)
        genre += songs.pop(song_to_pop) + " "
    return genre
#The function above and the ones following are repeats of the first function except with adjustments to the range each list contains since there is not the same number of songs contained in the filled out lists at the moment. I will fix this later though.

print create_genre(kpop)
print(*kpop, sep = "\n")

def create_genre(songs):
    genre = ""
    song_number = random.randint(0, 71)
    for item in range(0, song_number):
        song_to_pop = random.randint(0, len(songs) - 1)
        genre += songs.pop(song_to_pop) + " "
    return genre

print create_genre(r&b)
print(*r&b, sep = "\n")

def create_genre(songs):
    genre = ""
    song_number = random.randint(0, 78)
    for item in range(0, song_number):
        song_to_pop = random.randint(0, len(songs) - 1)
        genre += songs.pop(song_to_pop) + " "
    return genre

print create_genre(hip-hop)
print(*hip-hop, sep = "\n")

#Overall notes, I need some clarification on how each genre list could be selected and show songs from a single list. What I'm hoping is that through this pull method, each list would print songs from that specific list instead of combining songs from all of my lists together. Also, I would like to limit the number of songs printed at an instance to 10 songs instead of all the songs randomly printed out in the terminal. I'm unsure if it is even priting since repl.it won't let me sign in from GitHub.
