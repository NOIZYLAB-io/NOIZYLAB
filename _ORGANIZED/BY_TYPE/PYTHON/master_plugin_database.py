#!/usr/bin/env python3
"""
🎛️ MASTER PLUGIN & LIBRARY DATABASE
Complete database of ALL VST plugins, sample libraries, and audio tools
Knowledge base for intelligent organization
"""

# ==================== COMPREHENSIVE MANUFACTURER DATABASE ====================

MASTER_DATABASE = {
    
    # ==================== SAMPLE LIBRARIES ====================
    
    'Native Instruments': {
        'type': 'libraries',
        'keywords': ['native instruments', 'ni ', 'komplete', 'kontakt'],
        'products': {
            # Kontakt Libraries
            'Kontakt': ['Kontakt Factory Library', 'Kontakt Factory Selection'],
            'Komplete': ['Komplete 14', 'Komplete 13', 'Komplete Ultimate'],
            'Session': ['Session Strings', 'Session Horns', 'Session Guitarist', 'Session Ukulele'],
            'Scarbee': ['Scarbee Mark I', 'Scarbee A-200', 'Scarbee Funk Guitarist', 'Scarbee MM-Bass', 'Scarbee Jay-Bass', 'Scarbee Pre-Bass', 'Scarbee Rickenbacker Bass'],
            'The Giant': ['The Giant Piano'],
            'The Grandeur': ['The Grandeur Piano'],
            'Alicia Keys': ['Alicia\'s Keys'],
            'Vintage': ['Vintage Organs', 'Vintage Pianos'],
            'Action': ['Action Strikes', 'Action Strings'],
            'Damage': [],
            'Rise & Hit': [],
            'India': ['India Library'],
            'West Africa': ['West Africa Library'],
            'Middle East': ['Middle East Library'],
            'Cuba': ['Cuba Library'],
            'Balinese Gamelan': [],
            'Symphony Series': ['Symphony Essentials - Strings', 'Symphony Essentials - Brass', 'Symphony Essentials - Woodwinds', 'Symphony Essentials - Percussion'],
            'Noire': ['Noire Piano'],
            'Ethereal Earth': ['Ethereal Earth'],
            'Mysteria': [],
            'Straylight': ['Straylight'],
            'Kinetic': ['Kinetic Metal', 'Kinetic Toys'],
            'Ashlight': ['Ashlight'],
            'Molecule': [],
            'Flesh': [],
            'Form': [],
            'Kontour': [],
        }
    },
    
    'Spitfire Audio': {
        'type': 'libraries',
        'keywords': ['spitfire', 'albion', 'bbc'],
        'products': {
            'Albion': ['Albion One', 'Albion Neo', 'Albion Solstice', 'Albion Tundra', 'Albion Iceni'],
            'BBC': ['BBC Symphony Orchestra', 'BBC Symphony Orchestra Pro', 'BBC Symphony Orchestra Discover'],
            'Chamber': ['Chamber Strings', 'Chamber Brass', 'Chamber Evolutions'],
            'Studio': ['Studio Strings', 'Studio Brass', 'Studio Woodwinds', 'Studio Orchestra'],
            'Hans Zimmer': ['Hans Zimmer Strings', 'Hans Zimmer Percussion', 'Hans Zimmer Piano'],
            'Olafur Arnalds': ['Olafur Arnalds Composer Toolkit', 'Olafur Arnalds Chamber Evolutions', 'Olafur Arnalds Evolutions'],
            'Eric Whitacre': ['Eric Whitacre Choir'],
            'Phobos': [],
            'Originals': ['Epic Strings', 'Epic Brass', 'Cinematic Percussion', 'Firewood Piano'],
            'Labs': ['LABS (Free)'],
            'Symphonic': ['Symphonic Strings', 'Symphonic Brass', 'Symphonic Woodwinds', 'Symphonic Motions'],
        }
    },
    
    'Output': {
        'type': 'libraries',
        'keywords': ['output'],
        'products': {
            'Arcade': ['Arcade'],
            'Exhale': ['Exhale'],
            'Rev': ['Rev', 'Rev X-Loops'],
            'Signal': ['Signal'],
            'Movement': ['Movement'],
            'Analog': ['Analog Strings', 'Analog Brass & Winds'],
            'Substance': ['Substance Bass'],
            'Thermal': ['Thermal'],
            'Portal': ['Portal'],
        }
    },
    
    'Heavyocity': {
        'type': 'libraries',
        'keywords': ['heavyocity'],
        'products': {
            'Damage': ['Damage', 'Damage 2'],
            'Evolve': ['Evolve', 'Evolve Mutations', 'Evolve Mutations 2', 'Evolve Mutations 3', 'Evolve Mutations 4'],
            'Gravity': ['Gravity'],
            'Aeon': ['Aeon Collection'],
            'Mosaic': ['Mosaic Keys', 'Mosaic Pluck', 'Mosaic Warp'],
            'Master Sessions': ['Master Sessions Ensemble Drums', 'Master Sessions Ethnic Drum Ensembles'],
            'Symphonic': ['Symphonic Destruction'],
        }
    },
    
    'CineSamples': {
        'type': 'libraries',
        'keywords': ['cinesamples', 'cine'],
        'products': {
            'Brass': ['CineBrass Core', 'CineBrass Pro', 'CineBrass Descant Horns', 'CineBrass Sonore', 'CineBrass Twelve Horn Ensemble'],
            'Winds': ['CineWinds Core', 'CineWinds Pro', 'CineWinds Woodwinds Soloists'],
            'Strings': ['CineStrings CORE', 'CineStrings Solo'],
            'Percussion': ['CinePerc'],
            'Harps': ['CineHarps', 'CineHarp'],
            'Piano': ['Piano in Blue', 'Piano in 162'],
            'Voxos': ['Voxos Epic Choirs', 'Voxos 2'],
        }
    },
    
    'ProjectSAM': {
        'type': 'libraries',
        'keywords': ['project sam', 'projectsam', 'symphobia'],
        'products': {
            'Symphobia': ['Symphobia 1', 'Symphobia 2', 'Symphobia 3', 'Symphobia 4', 'Symphobia Colours Orchestrator'],
            'True Strike': ['True Strike 1', 'True Strike 2'],
            'Swing': ['Swing', 'Swing More'],
            'The Free Orchestra': ['The Free Orchestra'],
        }
    },
    
    'EastWest': {
        'type': 'libraries',
        'keywords': ['eastwest', 'east west', 'ew', 'quantum leap', 'hollywood'],
        'products': {
            'Hollywood': ['Hollywood Strings', 'Hollywood Brass', 'Hollywood Orchestral Woodwinds', 'Hollywood Orchestral Percussion', 'Hollywood Pop Brass', 'Hollywood Choirs', 'Hollywood Fantasy Voices', 'Hollywood Fantasy Orchestra'],
            'Stormdrum': ['Stormdrum', 'Stormdrum 2', 'Stormdrum 3'],
            'RA': ['RA'],
            'Silk': ['Silk'],
            'Ministry of Rock': ['Ministry of Rock 1', 'Ministry of Rock 2'],
            'Symphonic Orchestra': ['Symphonic Orchestra', 'Symphonic Orchestra Platinum', 'Symphonic Orchestra Gold'],
            'Quantum Leap': ['QL Pianos', 'QL Spaces', 'QL Gypsy'],
            'Goliath': [],
            'Fab Four': ['Fab Four'],
            'Voices of': ['Voices of Passion', 'Voices of the Empire', 'Voices of Opera'],
            'ProDrummer': ['ProDrummer 1', 'ProDrummer 2'],
        }
    },
    
    'Toontrack': {
        'type': 'libraries',
        'keywords': ['toontrack'],
        'products': {
            'Superior Drummer': ['Superior Drummer 3', 'Superior Drummer 2'],
            'EZdrummer': ['EZdrummer 2', 'EZdrummer 3'],
            'EZkeys': ['EZkeys', 'EZkeys 2'],
            'EZbass': ['EZbass'],
            'EZmix': ['EZmix 2', 'EZmix 3'],
            'SDX': ['Avatar', 'Music City USA', 'The Metal Foundry', 'Death & Darkness', 'Hitmaker', 'Roots', 'Custom & Vintage', 'Twisted Kit', 'Progressive Foundry'],
            'EZX': ['Pop Rock', 'Drumkit From Hell', 'Latin Percussion', 'Jazz', 'Metalheads', 'Nashville', 'Electronic'],
        }
    },
    
    '8Dio': {
        'type': 'libraries',
        'keywords': ['8dio'],
        'products': {
            'Adagio': ['Adagio Strings', 'Adagio Violins', 'Adagio Cellos', 'Adagio Basses'],
            'Century': ['Century Strings', 'Century Brass', 'Century Ostinato Strings'],
            'Intimate': ['Intimate Studio Strings'],
            'Claire': ['Claire Woodwinds', 'Claire Clarinet', 'Claire Flute'],
            'Requiem': ['Requiem Professional', 'Requiem Light'],
            'Lacrimosa': ['Lacrimosa'],
            'Anthology': ['Anthology Strings'],
            'Epic': ['Epic Dhol Drums', 'Epic Taikos', 'Epic Toms'],
        }
    },
    
    'Orchestral Tools': {
        'type': 'libraries',
        'keywords': ['orchestral tools'],
        'products': {
            'Berlin': ['Berlin Strings', 'Berlin Brass', 'Berlin Woodwinds', 'Berlin Percussion', 'Berlin Orchestra'],
            'Metropolis Ark': ['Metropolis Ark 1', 'Metropolis Ark 2', 'Metropolis Ark 3', 'Metropolis Ark 4', 'Metropolis Ark 5'],
            'Time': ['Time Macro', 'Time Micro'],
            'Tallinn': [],
            'Junkie': ['Junkie XL Brass', 'Junkie XL Drums'],
        }
    },
    
    'Soundiron': {
        'type': 'libraries',
        'keywords': ['soundiron'],
        'products': {
            'Olympus': ['Olympus Symphonic Choir', 'Olympus Micro Choir', 'Olympus Elements'],
            'Mars': ['Mars Symphonic Men\'s Choir'],
            'Venus': ['Venus Symphonic Women\'s Choir'],
            'Alto': ['Alto Flute', 'Alto Glockenspiel'],
            'Emotional': ['Emotional Piano', 'Emotional Cello'],
            'Lakeside': ['Lakeside Pipe Organ'],
            'Waterharp': ['Waterharp', 'Waterharp 2'],
            'Apocalypse': ['Apocalypse Percussion Ensemble'],
            'Voices': ['Voices of Rapture', 'Voices of Gaia'],
            'Circle': ['Circle Bells', 'Circle Chimes'],
            'Ancient': ['Ancient Greek Strings'],
        }
    },
    
    'Audio Imperia': {
        'type': 'libraries',
        'keywords': ['audio imperia', 'nucleus'],
        'products': {
            'Nucleus': ['Nucleus'],
            'Jaeger': ['Jaeger'],
            'Chorus': ['Chorus'],
            'Areia': ['Areia Lite'],
            'Talos': ['Talos'],
        }
    },
    
    'Embertone': {
        'type': 'libraries',
        'keywords': ['embertone'],
        'products': {
            'Violin': ['Friedlander Violin', 'Joshua Bell Violin'],
            'Cello': ['Blakus Cello'],
            'Trumpet': ['Chapman Trumpet'],
            'Saxophone': ['Sensual Saxophone'],
            'Walker': ['Walker 1959 Steinway D'],
            'Intimate': ['Intimate Strings LITE'],
        }
    },
    
    'Big Fish Audio': {
        'type': 'libraries',
        'keywords': ['big fish', 'bfa'],
        'products': {
            'Various': ['Street Beatz', 'Hip Hop Producer', 'Funk Soul Horns', 'Urban Collection', 'Latin Grooves']
        }
    },
    
    'Loopmasters': {
        'type': 'libraries',
        'keywords': ['loopmasters'],
        'products': {
            'Various': ['Tech House', 'Dubstep', 'Drum & Bass', 'House']
        }
    },
    
    'Sample Logic': {
        'type': 'libraries',
        'keywords': ['sample logic', 'samplelogic'],
        'products': {
            'Cinematic': ['Cinematic Guitars', 'Cinematic Keys', 'Cinematic Soundscapes'],
            'Morphestra': ['Morphestra', 'Morphestra 2'],
            'Cinemorphx': ['Cinemorphx'],
            'Arpology': ['Arpology Cinematic Dimensions'],
            'Bohemian': ['Bohemian Cello', 'Bohemian Violin'],
        }
    },
    
    'Best Service': {
        'type': 'libraries',
        'keywords': ['best service'],
        'products': {
            'Engine': ['Engine 2'],
            'ERA': ['ERA Medieval Legends', 'ERA II Vocal Codex'],
            'Chris Hein': ['Chris Hein Horns', 'Chris Hein Bass', 'Chris Hein Guitars'],
            'Galaxy': ['Galaxy Steinway', 'Galaxy X'],
        }
    },
    
    'Emergence Audio': {
        'type': 'libraries',
        'keywords': ['emergence'],
        'products': {
            'Django': ['Django Gypsy Jazz Guitar'],
            'Infinite': ['Infinite Woodwinds', 'Infinite Brass', 'Infinite Strings'],
        }
    },
    
    'Impact Soundworks': {
        'type': 'libraries',
        'keywords': ['impact soundworks'],
        'products': {
            'Shreddage': ['Shreddage 3', 'Shreddage Bass 2', 'Shreddage Drums'],
            'Ventus': ['Ventus Ethnic Winds', 'Ventus Woodwinds'],
            'Bravura': ['Bravura Scoring Brass'],
            'Rhapsody': ['Rhapsody Orchestral Percussion', 'Rhapsody Orchestral Colors'],
            'Tokyo': ['Tokyo Scoring Strings'],
        }
    },
    
    'Sonokinetic': {
        'type': 'libraries',
        'keywords': ['sonokinetic'],
        'products': {
            'Da Capo': ['Da Capo'],
            'Capriccio': ['Capriccio'],
            'Grosso': ['Grosso'],
            'Minimal': ['Minimal'],
            'Sotto': ['Sotto'],
            'Vivace': ['Vivace'],
            'Sultan': ['Sultan Drums'],
            'Noir': ['Noir'],
        }
    },
    
    'Wide Blue Sound': {
        'type': 'libraries',
        'keywords': ['wide blue sound'],
        'products': {
            'Orbit': ['Orbit'],
            'Eclipse': ['Eclipse'],
            'Proximity': ['Proximity'],
        }
    },
    
    'Audiobro': {
        'type': 'libraries',
        'keywords': ['audiobro'],
        'products': {
            'LASS': ['LA Scoring Strings 2', 'LA Scoring Strings 3'],
            'Modern': ['Modern Scoring Brass'],
            'Genesis': ['Genesis Children\'s Choir'],
        }
    },
    
    'Cinematique Instruments': {
        'type': 'libraries',
        'keywords': ['cinematique'],
        'products': {
            'Piano': ['Felt Piano', 'Deconstructed Piano'],
            'Strings': ['Solo Cello', 'Autoharp'],
            'Experimental': ['Klanghaus', 'Artisan'],
        }
    },
    
    # ==================== SFX LIBRARIES ====================
    
    'Hollywood Edge': {
        'type': 'sfx',
        'keywords': ['hollywood edge', 'he '],
        'products': {
            'Premiere Edition': ['Premiere Edition'],
            'Cartoon Trax': ['Cartoon Trax'],
            'Sound Effects Library': ['Sound Effects Library'],
        }
    },
    
    'Sound Ideas': {
        'type': 'sfx',
        'keywords': ['sound ideas', 'si ', 'soundideas'],
        'products': {
            'Series 6000': ['6000 General Sound Effects Library'],
            'Series 4000': ['4000 Hollywood Sound Effects'],
            'Series 8000': ['8000 Sci-Fi Sound Effects'],
            'Series 1000': ['1000 Sound Effects'],
        }
    },
    
    'BBC Sound Effects': {
        'type': 'sfx',
        'keywords': ['bbc'],
        'products': {
            'Original': ['BBC Sound Effects Library'],
            'Science Fiction': ['BBC Science Fiction Sound Effects'],
        }
    },
    
    'Boom Library': {
        'type': 'sfx',
        'keywords': ['boom library', 'boom'],
        'products': {
            'Cinematic': ['Cinematic Hits', 'Cinematic Trailers', 'Cinematic Metal'],
            'Creature': ['Creature', 'Creature Vocals'],
            'Debris': ['Construction', 'Destruction'],
            'Medieval': ['Medieval Weapons', 'Medieval Life'],
            'Sci-Fi': ['Sci-Fi Whooshes', 'Sci-Fi Weapons'],
        }
    },
    
    'Pro Sound Effects': {
        'type': 'sfx',
        'keywords': ['pro sound effects', 'pse'],
        'products': {
            'Hybrid Library': ['Hybrid Library'],
            'Master Library': ['Master Library'],
        }
    },
    
    # ==================== VST PLUGINS ====================
    
    'Arturia': {
        'type': 'vst',
        'keywords': ['arturia'],
        'products': {
            'V Collection': ['V Collection 9', 'V Collection 8'],
            'Synths': ['Analog Lab', 'Pigments', 'Mini V', 'Modular V', 'ARP 2600 V', 'Prophet V', 'Jupiter 8V', 'Jup-8 V4', 'CS-80 V', 'Matrix 12 V', 'Synthi V', 'CMI V'],
            'FX': ['FX Collection', 'Rev PLATE-140', 'Rev SPRING-636', 'Bus FORCE', 'Pre 1973', 'Pre TridA', 'Comp FET-76', 'Comp VCA-65'],
        }
    },
    
    'Waves': {
        'type': 'vst',
        'keywords': ['waves'],
        'products': {
            'Bundles': ['Gold', 'Platinum', 'Diamond', 'Mercury', 'Studio Classics', 'SSL Complete', 'Abbey Road Collection'],
            'Compressors': ['CLA-76', 'CLA-2A', 'CLA-3A', 'SSL Comp', 'API 2500', 'PuigChild', 'Kramer HLS', 'MV2'],
            'EQ': ['SSL E-Channel', 'SSL G-Channel', 'API 550', 'API 560', 'PuigTec EQP-1A', 'Renaissance EQ', 'Q10', 'H-EQ'],
            'Reverb': ['H-Reverb', 'Renaissance Reverb', 'Abbey Road Chambers', 'Abbey Road Reverb Plates', 'EMT 140'],
            'Delay': ['H-Delay', 'SuperTap', 'Manny Marroquin Delay'],
            'Saturation': ['J37 Tape', 'Kramer Master Tape', 'Abbey Road Saturator', 'Black Box Analog Design HG-2'],
            'Vocals': ['Vocal Rider', 'DeBreath', 'Sibilance', 'Clarity Vx', 'Clarity Vx Pro'],
            'Metering': ['WLM Plus', 'Dorrough', 'PAZ Analyzer'],
        }
    },
    
    'FabFilter': {
        'type': 'vst',
        'keywords': ['fabfilter'],
        'products': {
            'Bundle': ['Total Bundle'],
            'EQ': ['Pro-Q 3', 'Pro-Q 2'],
            'Compressor': ['Pro-C 2'],
            'Limiter': ['Pro-L 2'],
            'Gate': ['Pro-G'],
            'MB': ['Pro-MB'],
            'DS': ['Pro-DS'],
            'R': ['Pro-R'],
            'Saturn': ['Saturn 2'],
            'Timeless': ['Timeless 3'],
            'Volcano': ['Volcano 3'],
            'One': ['One'],
            'Twin': ['Twin 3'],
        }
    },
    
    'iZotope': {
        'type': 'vst',
        'keywords': ['izotope'],
        'products': {
            'Bundles': ['Music Production Suite', 'Post Production Suite', 'Everything Bundle'],
            'Ozone': ['Ozone 11', 'Ozone 10', 'Ozone Advanced'],
            'Neutron': ['Neutron 4', 'Neutron 3'],
            'Nectar': ['Nectar 4', 'Nectar 3'],
            'RX': ['RX 11', 'RX 10', 'RX Advanced'],
            'Insight': ['Insight 2'],
            'VocalSynth': ['VocalSynth 2'],
            'Trash': ['Trash 2'],
            'Iris': ['Iris 2'],
            'Stutter': ['Stutter Edit 2'],
        }
    },
    
    'UAD (Universal Audio)': {
        'type': 'vst',
        'keywords': ['uad', 'universal audio'],
        'products': {
            'Compressors': ['1176', '1176LN', 'LA-2A', 'LA-3A', 'Fairchild 660', 'Fairchild 670', 'Distressor', 'dbx 160'],
            'EQ': ['Neve 1073', 'Neve 1081', 'Neve 88RS', 'API Vision', 'Manley Massive Passive', 'Pultec EQP-1A', 'Pultec MEQ-5'],
            'Preamps': ['Neve Preamp', 'API Preamp', 'SSL E Channel', 'SSL G Channel'],
            'Reverb': ['Capitol Chambers', 'EMT 140', 'EMT 250', 'Lexicon 224'],
            'Tape': ['Ampex ATR-102', 'Studer A800', 'Oxide Tape'],
            'Channel Strips': ['Neve 1073', 'Neve 1084', 'API Vision', 'SSL 4000 E', 'SSL 4000 G'],
        }
    },
    
    'Plugin Alliance': {
        'type': 'vst',
        'keywords': ['plugin alliance', 'brainworx'],
        'products': {
            'Brainworx': ['bx_console SSL 4000 E', 'bx_console SSL 4000 G', 'bx_console N', 'bx_digital V3'],
            'Lindell': ['Lindell 80 Series', 'Lindell PEX-500'],
            'SPL': ['SPL TwinTube', 'SPL Transient Designer', 'SPL De-Esser'],
            'Elysia': ['nvelope', 'mpressor', 'alpha compressor'],
            'Shadow Hills': ['Shadow Hills Mastering Compressor'],
            'Maag': ['Maag EQ4'],
            'Dangerous': ['Dangerous BAX EQ'],
        }
    },
    
    'Slate Digital': {
        'type': 'vst',
        'keywords': ['slate digital'],
        'products': {
            'Bundle': ['All Access Pass'],
            'Virtual': ['Virtual Mix Rack', 'Virtual Channel', 'Virtual Tape Machines', 'Virtual Console Collection', 'Virtual Buss Compressors'],
            'FG': ['FG-X Mastering Processor', 'FG-Stress', 'FG-N Compressor', 'FG-A Compressor', 'FG-116 Compressor', 'FG-2A Compressor'],
            'Fresh Air': [],
            'Virtual Preamp Collection': [],
        }
    },
    
    'Soundtoys': {
        'type': 'vst',
        'keywords': ['soundtoys'],
        'products': {
            'Bundle': ['Soundtoys 5'],
            'Decapitator': [],
            'EchoBoy': [],
            'PrimalTap': [],
            'FilterFreak': [],
            'Tremolator': [],
            'PanMan': [],
            'PhaseMistress': [],
            'Crystallizer': [],
            'Little': ['Little AlterBoy', 'Little Plate', 'Little MicroShift'],
            'Devil': ['Devil-Loc', 'Devil-Loc Deluxe'],
        }
    },
    
    'Valhalla DSP': {
        'type': 'vst',
        'keywords': ['valhalla'],
        'products': {
            'VintageVerb': [],
            'Room': [],
            'Plate': [],
            'Shimmer': [],
            'Delay': [],
            'Freq Echo': [],
            'Supermassive': [],
            'SpaceModulator': [],
        }
    },
    
    'Xfer Records': {
        'type': 'vst',
        'keywords': ['xfer', 'serum'],
        'products': {
            'Serum': [],
            'Nerve': [],
            'Cthulhu': [],
            'OTT': [],
            'LFOTool': [],
        }
    },
    
    'Spectrasonics': {
        'type': 'vst',
        'keywords': ['spectrasonics'],
        'products': {
            'Omnisphere': ['Omnisphere 2'],
            'Trilian': [],
            'Keyscape': [],
            'Stylus RMX': [],
        }
    },
    
    'u-he': {
        'type': 'vst',
        'keywords': ['u-he', 'uhe'],
        'products': {
            'Diva': [],
            'Repro': ['Repro-1', 'Repro-5'],
            'Zebra': ['Zebra2', 'ZebraHZ'],
            'Hive': ['Hive 2'],
            'Satin': [],
            'Presswerk': [],
            'Twangström': [],
            'Uhbik': [],
            'MFM2': [],
        }
    },
    
    'Lennar Digital': {
        'type': 'vst',
        'keywords': ['sylenth', 'lennardigital'],
        'products': {
            'Sylenth1': [],
        }
    },
    
    'Reveal Sound': {
        'type': 'vst',
        'keywords': ['spire'],
        'products': {
            'Spire': [],
        }
    },
    
    'Tone2': {
        'type': 'vst',
        'keywords': ['tone2'],
        'products': {
            'Electra': ['ElectraX', 'Electra2'],
            'Saurus': ['Saurus'],
            'Icarus': [],
            'RayBlaster': [],
        }
    },
    
    'Celemony': {
        'type': 'vst',
        'keywords': ['melodyne', 'celemony'],
        'products': {
            'Melodyne': ['Melodyne 5 Studio', 'Melodyne 5 Editor', 'Melodyne 5 Essential'],
        }
    },
    
    'Synchro Arts': {
        'type': 'vst',
        'keywords': ['vocalign', 'revoice'],
        'products': {
            'VocALign': ['VocALign Pro', 'VocALign Ultra'],
            'Revoice': ['Revoice Pro 4'],
        }
    },
    
    'Avid': {
        'type': 'vst',
        'keywords': ['avid', 'pro tools'],
        'products': {
            'Pro Tools': ['Pro Tools Ultimate', 'Pro Tools Studio'],
        }
    },
    
}

# ==================== KONTAKT FORMATS ====================
KONTAKT_EXTENSIONS = {
    '.nki': 'Kontakt Instrument',
    '.nkm': 'Kontakt Multi',
    '.nkc': 'Kontakt Compressed Sample',
    '.nkr': 'Kontakt Resources',
    '.ncw': 'Kontakt Compressed Wave',
    '.nkx': 'Kontakt Encrypted Sample',
    '.nka': 'Kontakt Archive',
    '.nksn': 'Native Kontrol Standard Snapshot',
}

# ==================== COMMON FILE FORMATS ====================
AUDIO_FORMATS = {
    '.wav': 'WAV Audio',
    '.aif': 'AIFF Audio',
    '.aiff': 'AIFF Audio',
    '.mp3': 'MP3 Audio',
    '.flac': 'FLAC Audio',
    '.ogg': 'OGG Vorbis',
    '.m4a': 'M4A Audio',
    '.wma': 'Windows Media Audio',
    '.alac': 'Apple Lossless',
}

SAMPLER_FORMATS = {
    '.exs': 'EXS24 Instrument',
    '.sxt': 'HALion Instrument',
    '.sfz': 'SFZ Instrument',
    '.gig': 'Gigastudio',
    '.sf2': 'SoundFont 2',
    '.dls': 'Downloadable Sounds',
    '.bnk': 'AKAI Bank',
}

PRESET_FORMATS = {
    '.fxp': 'VST Preset',
    '.fxb': 'VST Bank',
    '.vstpreset': 'VST3 Preset',
    '.aupreset': 'Audio Unit Preset',
    '.h2p': 'Native Instruments Preset',
}

# ==================== HELPER FUNCTIONS ====================

def get_manufacturer_info(library_name: str):
    """Get manufacturer information from library name"""
    library_lower = library_name.lower()
    
    for manufacturer, info in MASTER_DATABASE.items():
        for keyword in info['keywords']:
            if keyword.lower() in library_lower:
                return {
                    'manufacturer': manufacturer,
                    'type': info['type'],
                    'original_name': library_name
                }
    
    return {
        'manufacturer': 'Unknown',
        'type': 'unknown',
        'original_name': library_name
    }

def get_all_manufacturers():
    """Get list of all manufacturers"""
    return sorted(MASTER_DATABASE.keys())

def get_manufacturers_by_type(type_filter):
    """Get manufacturers filtered by type"""
    return [
        name for name, info in MASTER_DATABASE.items()
        if info['type'] == type_filter
    ]

def search_products(query: str):
    """Search for products across all manufacturers"""
    results = []
    query_lower = query.lower()
    
    for manufacturer, info in MASTER_DATABASE.items():
        if query_lower in manufacturer.lower():
            results.append({
                'manufacturer': manufacturer,
                'type': info['type'],
                'match_type': 'manufacturer'
            })
        
        for category, products in info.get('products', {}).items():
            if query_lower in category.lower():
                results.append({
                    'manufacturer': manufacturer,
                    'category': category,
                    'type': info['type'],
                    'match_type': 'category'
                })
            
            for product in products:
                if query_lower in product.lower():
                    results.append({
                        'manufacturer': manufacturer,
                        'product': product,
                        'category': category,
                        'type': info['type'],
                        'match_type': 'product'
                    })
    
    return results

if __name__ == "__main__":
    print("🎛️ MASTER PLUGIN & LIBRARY DATABASE")
    print("="*80)
    print(f"\nTotal Manufacturers: {len(MASTER_DATABASE)}")
    print(f"Libraries: {len(get_manufacturers_by_type('libraries'))}")
    print(f"SFX: {len(get_manufacturers_by_type('sfx'))}")
    print(f"VST Plugins: {len(get_manufacturers_by_type('vst'))}")
    print("\n" + "="*80)

