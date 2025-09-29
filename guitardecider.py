x=str(input("enter the name of the desired guitar : "))
guitar_models = [

    ("fender stratocaster", "Fender Stratocaster"),
    ("fender stratocaster standard", "Fender Stratocaster Standard"),
    ("fender stratocaster deluxe", "Fender Stratocaster Deluxe"),
    ("fender stratocaster american professional", "Fender Stratocaster American Professional"),
    ("fender stratocaster american ultra", "Fender Stratocaster American Ultra"),
    ("fender stratocaster player", "Fender Stratocaster Player"),
    ("fender stratocaster hss", "Fender Stratocaster HSS"),
    ("fender stratocaster hh", "Fender Stratocaster HH"),
    ("fender stratocaster custom shop", "Fender Stratocaster Custom Shop"),
    ("fender stratocaster eric clapton", "Fender Stratocaster Eric Clapton"),
    ("fender stratocaster david gilmour", "Fender Stratocaster David Gilmour"),
    ("fender stratocaster yngwie malmsteen", "Fender Stratocaster Yngwie Malmsteen"),

 
    ("fender telecaster", "Fender Telecaster"),
    ("fender telecaster standard", "Fender Telecaster Standard"),
    ("fender telecaster deluxe", "Fender Telecaster Deluxe"),
    ("fender telecaster thinline", "Fender Telecaster Thinline"),
    ("fender telecaster custom", "Fender Telecaster Custom"),
    ("fender telecaster american professional", "Fender Telecaster American Professional"),
    ("fender telecaster player", "Fender Telecaster Player"),
    ("fender telecaster jim root", "Fender Telecaster Jim Root"),
    ("fender telecaster george harrison rosewood", "Fender Telecaster George Harrison Rosewood"),


    ("fender jaguar", "Fender Jaguar"),
    ("fender jazzmaster", "Fender Jazzmaster"),
    ("fender mustang", "Fender Mustang"),
    ("fender duo-sonic", "Fender Duo-Sonic"),

  
    ("gibson les paul standard", "Gibson Les Paul Standard"),
    ("gibson les paul classic", "Gibson Les Paul Classic"),
    ("gibson les paul traditional", "Gibson Les Paul Traditional"),
    ("gibson les paul custom", "Gibson Les Paul Custom"),
    ("gibson les paul junior", "Gibson Les Paul Junior"),
    ("gibson les paul studio", "Gibson Les Paul Studio"),
    ("gibson les paul tribute", "Gibson Les Paul Tribute"),
    ("gibson les paul modern", "Gibson Les Paul Modern"),
    ("gibson les paul slash", "Gibson Les Paul Slash"),
    ("gibson les paul joe perry", "Gibson Les Paul Joe Perry"),
    ("gibson les paul r9", "Gibson Les Paul R9"),

   
    ("gibson sg standard", "Gibson SG Standard"),
    ("gibson sg special", "Gibson SG Special"),
    ("gibson sg junior", "Gibson SG Junior"),
    ("gibson sg modern", "Gibson SG Modern"),
    ("gibson sg custom", "Gibson SG Custom"),
    ("gibson sg angus young", "Gibson SG Angus Young"),
    ("gibson sg tony iommi", "Gibson SG Tony Iommi"),

   
    ("gibson es-335", "Gibson ES-335"),
    ("gibson es-339", "Gibson ES-339"),
    ("gibson es-175", "Gibson ES-175"),
    ("gibson es-137", "Gibson ES-137"),
    ("gibson es-330", "Gibson ES-330"),

    ("gibson flying v", "Gibson Flying V"),
    ("gibson explorer", "Gibson Explorer"),
    ("gibson firebird", "Gibson Firebird"),
    ("gibson melody maker", "Gibson Melody Maker"),
    ("gibson l-5", "Gibson L-5"),

   
    ("prs custom 24", "PRS Custom 24"),
    ("prs custom 22", "PRS Custom 22"),
    ("prs silver sky", "PRS Silver Sky"),
    ("prs mccarty 594", "PRS McCarty 594"),
    ("prs santana", "PRS Santana"),
    ("prs se custom 24", "PRS SE Custom 24"),
    ("prs se paul’s guitar", "PRS SE Paul's Guitar"),

 
    ("ibanez rg", "Ibanez RG"),
    ("ibanez jem", "Ibanez JEM"),
    ("ibanez s series", "Ibanez S Series"),
    ("ibanez artist", "Ibanez Artist"),
    ("ibanez iceman", "Ibanez Iceman"),
    ("ibanez destroyer", "Ibanez Destroyer"),
    ("ibanez artcore", "Ibanez Artcore"),
    ("ibanez prestige", "Ibanez Prestige"),
    ("ibanez gio", "Ibanez GIO"),

    ("esp eclipse", "ESP Eclipse"),
    ("esp horizon", "ESP Horizon"),
    ("esp viper", "ESP Viper"),
    ("esp mh", "ESP MH"),
    ("esp ltd ec-1000", "ESP LTD EC-1000"),
    ("esp ltd mh-1000", "ESP LTD MH-1000"),
    ("esp ltd viper-1000", "ESP LTD Viper-1000"),
    ("esp kirk hammett kh-2", "ESP Kirk Hammett KH-2"),
    ("esp james hetfield snakebyte", "ESP James Hetfield Snakebyte"),

    ("jackson soloist", "Jackson Soloist"),
    ("jackson dinky", "Jackson Dinky"),
    ("jackson rhoads", "Jackson Rhoads"),
    ("jackson kelly", "Jackson Kelly"),

    ("gretsch white falcon", "Gretsch White Falcon"),
    ("gretsch duo jet", "Gretsch Duo Jet"),
    ("gretsch country gentleman", "Gretsch Country Gentleman"),
    ("gretsch electromatic", "Gretsch Electromatic"),

    ("rickenbacker 360", "Rickenbacker 360"),
    ("rickenbacker 330", "Rickenbacker 330"),
    ("rickenbacker 620", "Rickenbacker 620"),
    ("rickenbacker 4001", "Rickenbacker 4001"),
    ("rickenbacker 4003", "Rickenbacker 4003"),

   
    ("yamaha revstar", "Yamaha Revstar"),
    ("yamaha pacifica", "Yamaha Pacifica"),
    ("yamaha sg2000", "Yamaha SG2000"),
    ("yamaha c40", "Yamaha C40"),

    
    ("epiphone casino", "Epiphone Casino"),
    ("epiphone dot", "Epiphone Dot"),
    ("epiphone sheraton", "Epiphone Sheraton"),
    ("epiphone les paul standard", "Epiphone Les Paul Standard"),
    ("epiphone g-400", "Epiphone G-400"),
    ("epiphone es-339", "Epiphone ES-339"),


    ("schecter hellraiser", "Schecter Hellraiser"),
    ("schecter c-1", "Schecter C-1"),
    ("schecter omen 6", "Schecter Omen 6"),
    ("schecter blackjack", "Schecter Blackjack"),
    ("schecter avenger", "Schecter Avenger"),

   
    ("martin d-28", "Martin D-28"),
    ("martin d-18", "Martin D-18"),
    ("martin 000-28", "Martin 000-28"),
    ("martin om-28", "Martin OM-28"),
    ("martin 000-15m", "Martin 000-15M"),
    ("martin d-45", "Martin D-45"),

    ("taylor 814ce", "Taylor 814ce"),
    ("taylor 214ce", "Taylor 214ce"),
    ("taylor gs mini", "Taylor GS Mini"),
    ("taylor baby", "Taylor Baby"),
    ("taylor 110e", "Taylor 110e"),

    
    ("guild starfire", "Guild Starfire"),
    ("guild d-55", "Guild D-55"),
    ("guild f-512", "Guild F-512"),

    
    ("seagull s6", "Seagull S6"),
    ("seagull entourage", "Seagull Entouraage"),

   
    ("ovation celebrity", "Ovation Celebrity"),
    ("ovation elite", "Ovation Elite"),

   
    ("takamine gd30", "Takamine GD30"),
    ("takamine p3dc", "Takamine P3DC"),

   
    ("cordoba c5", "Cordoba C5"),
    ("cordoba c7", "Cordoba C7"),
    ("cordoba fusion 12", "Cordoba Fusion 12"),

   
    ("fender precision bass", "Fender Precision Bass"),
    ("fender jazz bass", "Fender Jazz Bass"),
    ("fender mustang bass", "Fender Mustang Bass"),
    ("gibson thunderbird", "Gibson Thunderbird"),
    ("music man stingray", "Music Man StingRay"),
    ("ibanez sr", "Ibanez SR"),
    ("ibanez atk", "Ibanez ATK"),
    ("warwick corvette", "Warwick Corvette"),
    ("spector euro", "Spector Euro"),
    ("rickebacker 4003", "Rickenbacker 4003")
]

