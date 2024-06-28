from enum import Enum

class MovesEnum(Enum):
    MovesEnum_DICT = {
        'moves': {
            'NONE': 0,
            'POUND': 1,
            'KARATE_CHOP': 2,
            'DOUBLE_SLAP': 3,
            'COMET_PUNCH': 4,
            'MEGA_PUNCH': 5,
            'PAY_DAY': 6,
            'FIRE_PUNCH': 7,
            'ICE_PUNCH': 8,
            'THUNDER_PUNCH': 9,
            'SCRATCH': 10,
            'VISE_GRIP': 11,
            'GUILLOTINE': 12,
            'RAZOR_WIND': 13,
            'SWORDS_DANCE': 14,
            'CUT': 15,
            'GUST': 16,
            'WING_ATTACK': 17,
            'WHIRLWIND': 18,
            'FLY': 19,
            'BIND': 20,
            'SLAM': 21,
            'VINE_WHIP': 22,
            'STOMP': 23,
            'DOUBLE_KICK': 24,
            'MEGA_KICK': 25,
            'JUMP_KICK': 26,
            'ROLLING_KICK': 27,
            'SAND_ATTACK': 28,
            'HEADBUTT': 29,
            'HORN_ATTACK': 30,
            'FURY_ATTACK': 31,
            'HORN_DRILL': 32,
            'TACKLE': 33,
            'BODY_SLAM': 34,
            'WRAP': 35,
            'TAKE_DOWN': 36,
            'THRASH': 37,
            'DOUBLE_EDGE': 38,
            'TAIL_WHIP': 39,
            'POISON_STING': 40,
            'TWINEEDLE': 41,
            'PIN_MISSILE': 42,
            'LEER': 43,
            'BITE': 44,
            'GROWL': 45,
            'ROAR': 46,
            'SING': 47,
            'SUPERSONIC': 48,
            'SONIC_BOOM': 49,
            'DISABLE': 50,
            'ACID': 51,
            'EMBER': 52,
            'FLAMETHROWER': 53,
            'MIST': 54,
            'WATER_GUN': 55,
            'HYDRO_PUMP': 56,
            'SURF': 57,
            'ICE_BEAM': 58,
            'BLIZZARD': 59,
            'PSYBEAM': 60,
            'BUBBLE_BEAM': 61,
            'AURORA_BEAM': 62,
            'HYPER_BEAM': 63,
            'PECK': 64,
            'DRILL_PECK': 65,
            'SUBMISSION': 66,
            'LOW_KICK': 67,
            'COUNTER': 68,
            'SEISMIC_TOSS': 69,
            'STRENGTH': 70,
            'ABSORB': 71,
            'MEGA_DRAIN': 72,
            'LEECH_SEED': 73,
            'GROWTH': 74,
            'RAZOR_LEAF': 75,
            'SOLAR_BEAM': 76,
            'POISON_POWDER': 77,
            'STUN_SPORE': 78,
            'SLEEP_POWDER': 79,
            'PETAL_DANCE': 80,
            'STRING_SHOT': 81,
            'DRAGON_RAGE': 82,
            'FIRE_SPIN': 83,
            'THUNDER_SHOCK': 84,
            'THUNDERBOLT': 85,
            'THUNDER_WAVE': 86,
            'THUNDER': 87,
            'ROCK_THROW': 88,
            'EARTHQUAKE': 89,
            'FISSURE': 90,
            'DIG': 91,
            'TOXIC': 92,
            'CONFUSION': 93,
            'PSYCHIC': 94,
            'HYPNOSIS': 95,
            'MEDITATE': 96,
            'AGILITY': 97,
            'QUICK_ATTACK': 98,
            'RAGE': 99,
            'TELEPORT': 100,
            'NIGHT_SHADE': 101,
            'MIMIC': 102,
            'SCREECH': 103,
            'DOUBLE_TEAM': 104,
            'RECOVER': 105,
            'HARDEN': 106,
            'MINIMIZE': 107,
            'SMOKESCREEN': 108,
            'CONFUSE_RAY': 109,
            'WITHDRAW': 110,
            'DEFENSE_CURL': 111,
            'BARRIER': 112,
            'LIGHT_SCREEN': 113,
            'HAZE': 114,
            'REFLECT': 115,
            'FOCUS_ENERGY': 116,
            'BIDE': 117,
            'METRONOME': 118,
            'MIRROR_MOVE': 119,
            'SELF_DESTRUCT': 120,
            'EGG_BOMB': 121,
            'LICK': 122,
            'SMOG': 123,
            'SLUDGE': 124,
            'BONE_CLUB': 125,
            'FIRE_BLAST': 126,
            'WATERFALL': 127,
            'CLAMP': 128,
            'SWIFT': 129,
            'SKULL_BASH': 130,
            'SPIKE_CANNON': 131,
            'CONSTRICT': 132,
            'AMNESIA': 133,
            'KINESIS': 134,
            'SOFT_BOILED': 135,
            'HIGH_JUMP_KICK': 136,
            'GLARE': 137,
            'DREAM_EATER': 138,
            'POISON_GAS': 139,
            'BARRAGE': 140,
            'LEECH_LIFE': 141,
            'LOVELY_KISS': 142,
            'SKY_ATTACK': 143,
            'TRANSFORM': 144,
            'BUBBLE': 145,
            'DIZZY_PUNCH': 146,
            'SPORE': 147,
            'FLASH': 148,
            'PSYWAVE': 149,
            'SPLASH': 150,
            'ACID_ARMOR': 151,
            'CRABHAMMER': 152,
            'EXPLOSION': 153,
            'FURY_SWIPES': 154,
            'BONEMERANG': 155,
            'REST': 156,
            'ROCK_SLIDE': 157,
            'HYPER_FANG': 158,
            'SHARPEN': 159,
            'CONVERSION': 160,
            'TRI_ATTACK': 161,
            'SUPER_FANG': 162,
            'SLASH': 163,
            'SUBSTITUTE': 164,
            'STRUGGLE': 165,
            'SKETCH': 166,
            'TRIPLE_KICK': 167,
            'THIEF': 168,
            'SPIDER_WEB': 169,
            'MIND_READER': 170,
            'NIGHTMARE': 171,
            'FLAME_WHEEL': 172,
            'SNORE': 173,
            'CURSE': 174,
            'FLAIL': 175,
            'CONVERSION_2': 176,
            'AEROBLAST': 177,
            'COTTON_SPORE': 178,
            'REVERSAL': 179,
            'SPITE': 180,
            'POWDER_SNOW': 181,
            'PROTECT': 182,
            'MACH_PUNCH': 183,
            'SCARY_FACE': 184,
            'FEINT_ATTACK': 185,
            'SWEET_KISS': 186,
            'BELLY_DRUM': 187,
            'SLUDGE_BOMB': 188,
            'MUD_SLAP': 189,
            'OCTAZOOKA': 190,
            'SPIKES': 191,
            'ZAP_CANNON': 192,
            'FORESIGHT': 193,
            'DESTINY_BOND': 194,
            'PERISH_SONG': 195,
            'ICY_WIND': 196,
            'DETECT': 197,
            'BONE_RUSH': 198,
            'LOCK_ON': 199,
            'OUTRAGE': 200,
            'SANDSTORM': 201,
            'GIGA_DRAIN': 202,
            'ENDURE': 203,
            'CHARM': 204,
            'ROLLOUT': 205,
            'FALSE_SWIPE': 206,
            'SWAGGER': 207,
            'MILK_DRINK': 208,
            'SPARK': 209,
            'FURY_CUTTER': 210,
            'STEEL_WING': 211,
            'MEAN_LOOK': 212,
            'ATTRACT': 213,
            'SLEEP_TALK': 214,
            'HEAL_BELL': 215,
            'RETURN': 216,
            'PRESENT': 217,
            'FRUSTRATION': 218,
            'SAFEGUARD': 219,
            'PAIN_SPLIT': 220,
            'SACRED_FIRE': 221,
            'MAGNITUDE': 222,
            'DYNAMIC_PUNCH': 223,
            'MEGAHORN': 224,
            'DRAGON_BREATH': 225,
            'BATON_PASS': 226,
            'ENCORE': 227,
            'PURSUIT': 228,
            'RAPID_SPIN': 229,
            'SWEET_SCENT': 230,
            'IRON_TAIL': 231,
            'METAL_CLAW': 232,
            'VITAL_THROW': 233,
            'MORNING_SUN': 234,
            'SYNTHESIS': 235,
            'MOONLIGHT': 236,
            'HIDDEN_POWER': 237,
            'CROSS_CHOP': 238,
            'TWISTER': 239,
            'RAIN_DANCE': 240,
            'SUNNY_DAY': 241,
            'CRUNCH': 242,
            'MIRROR_COAT': 243,
            'PSYCH_UP': 244,
            'EXTREME_SPEED': 245,
            'ANCIENT_POWER': 246,
            'SHADOW_BALL': 247,
            'FUTURE_SIGHT': 248,
            'ROCK_SMASH': 249,
            'WHIRLPOOL': 250,
            'BEAT_UP': 251,
            'FAKE_OUT': 252,
            'UPROAR': 253,
            'STOCKPILE': 254,
            'SPIT_UP': 255,
            'SWALLOW': 256,
            'HEAT_WAVE': 257,
            'HAIL': 258,
            'TORMENT': 259,
            'FLATTER': 260,
            'WILL_O_WISP': 261,
            'MEMENTO': 262,
            'FACADE': 263,
            'FOCUS_PUNCH': 264,
            'SMELLING_SALTS': 265,
            'FOLLOW_ME': 266,
            'NATURE_POWER': 267,
            'CHARGE': 268,
            'TAUNT': 269,
            'HELPING_HAND': 270,
            'TRICK': 271,
            'ROLE_PLAY': 272,
            'WISH': 273,
            'ASSIST': 274,
            'INGRAIN': 275,
            'SUPERPOWER': 276,
            'MAGIC_COAT': 277,
            'RECYCLE': 278,
            'REVENGE': 279,
            'BRICK_BREAK': 280,
            'YAWN': 281,
            'KNOCK_OFF': 282,
            'ENDEAVOR': 283,
            'ERUPTION': 284,
            'SKILL_SWAP': 285,
            'IMPRISON': 286,
            'REFRESH': 287,
            'GRUDGE': 288,
            'SNATCH': 289,
            'SECRET_POWER': 290,
            'DIVE': 291,
            'ARM_THRUST': 292,
            'CAMOUFLAGE': 293,
            'TAIL_GLOW': 294,
            'LUSTER_PURGE': 295,
            'MIST_BALL': 296,
            'FEATHER_DANCE': 297,
            'TEETER_DANCE': 298,
            'BLAZE_KICK': 299,
            'MUD_SPORT': 300,
            'ICE_BALL': 301,
            'NEEDLE_ARM': 302,
            'SLACK_OFF': 303,
            'HYPER_VOICE': 304,
            'POISON_FANG': 305,
            'CRUSH_CLAW': 306,
            'BLAST_BURN': 307,
            'HYDRO_CANNON': 308,
            'METEOR_MASH': 309,
            'ASTONISH': 310,
            'WEATHER_BALL': 311,
            'AROMATHERAPY': 312,
            'FAKE_TEARS': 313,
            'AIR_CUTTER': 314,
            'OVERHEAT': 315,
            'ODOR_SLEUTH': 316,
            'ROCK_TOMB': 317,
            'SILVER_WIND': 318,
            'METAL_SOUND': 319,
            'GRASS_WHISTLE': 320,
            'TICKLE': 321,
            'COSMIC_POWER': 322,
            'WATER_SPOUT': 323,
            'SIGNAL_BEAM': 324,
            'SHADOW_PUNCH': 325,
            'EXTRASENSORY': 326,
            'SKY_UPPERCUT': 327,
            'SAND_TOMB': 328,
            'SHEER_COLD': 329,
            'MUDDY_WATER': 330,
            'BULLET_SEED': 331,
            'AERIAL_ACE': 332,
            'ICICLE_SPEAR': 333,
            'IRON_DEFENSE': 334,
            'BLOCK': 335,
            'HOWL': 336,
            'DRAGON_CLAW': 337,
            'FRENZY_PLANT': 338,
            'BULK_UP': 339,
            'BOUNCE': 340,
            'MUD_SHOT': 341,
            'POISON_TAIL': 342,
            'COVET': 343,
            'VOLT_TACKLE': 344,
            'MAGICAL_LEAF': 345,
            'WATER_SPORT': 346,
            'CALM_MIND': 347,
            'LEAF_BLADE': 348,
            'DRAGON_DANCE': 349,
            'ROCK_BLAST': 350,
            'SHOCK_WAVE': 351,
            'WATER_PULSE': 352,
            'DOOM_DESIRE': 353,
            'PSYCHO_BOOST': 354,
            'ROOST': 355,
            'GRAVITY': 356,
            'MIRACLE_EYE': 357,
            'WAKE_UP_SLAP': 358,
            'HAMMER_ARM': 359,
            'GYRO_BALL': 360,
            'HEALING_WISH': 361,
            'BRINE': 362,
            'NATURAL_GIFT': 363,
            'FEINT': 364,
            'PLUCK': 365,
            'TAILWIND': 366,
            'ACUPRESSURE': 367,
            'METAL_BURST': 368,
            'U_TURN': 369,
            'CLOSE_COMBAT': 370,
            'PAYBACK': 371,
            'ASSURANCE': 372,
            'EMBARGO': 373,
            'FLING': 374,
            'PSYCHO_SHIFT': 375,
            'TRUMP_CARD': 376,
            'HEAL_BLOCK': 377,
            'WRING_OUT': 378,
            'POWER_TRICK': 379,
            'GASTRO_ACID': 380,
            'LUCKY_CHANT': 381,
            'ME_FIRST': 382,
            'COPYCAT': 383,
            'POWER_SWAP': 384,
            'GUARD_SWAP': 385,
            'PUNISHMENT': 386,
            'LAST_RESORT': 387,
            'WORRY_SEED': 388,
            'SUCKER_PUNCH': 389,
            'TOXIC_SPIKES': 390,
            'HEART_SWAP': 391,
            'AQUA_RING': 392,
            'MAGNET_RISE': 393,
            'FLARE_BLITZ': 394,
            'FORCE_PALM': 395,
            'AURA_SPHERE': 396,
            'ROCK_POLISH': 397,
            'POISON_JAB': 398,
            'DARK_PULSE': 399,
            'NIGHT_SLASH': 400,
            'AQUA_TAIL': 401,
            'SEED_BOMB': 402,
            'AIR_SLASH': 403,
            'X_SCISSOR': 404,
            'BUG_BUZZ': 405,
            'DRAGON_PULSE': 406,
            'DRAGON_RUSH': 407,
            'POWER_GEM': 408,
            'DRAIN_PUNCH': 409,
            'VACUUM_WAVE': 410,
            'FOCUS_BLAST': 411,
            'ENERGY_BALL': 412,
            'BRAVE_BIRD': 413,
            'EARTH_POWER': 414,
            'SWITCHEROO': 415,
            'GIGA_IMPACT': 416,
            'NASTY_PLOT': 417,
            'BULLET_PUNCH': 418,
            'AVALANCHE': 419,
            'ICE_SHARD': 420,
            'SHADOW_CLAW': 421,
            'THUNDER_FANG': 422,
            'ICE_FANG': 423,
            'FIRE_FANG': 424,
            'SHADOW_SNEAK': 425,
            'MUD_BOMB': 426,
            'PSYCHO_CUT': 427,
            'ZEN_HEADBUTT': 428,
            'MIRROR_SHOT': 429,
            'FLASH_CANNON': 430,
            'ROCK_CLIMB': 431,
            'DEFOG': 432,
            'TRICK_ROOM': 433,
            'DRACO_METEOR': 434,
            'DISCHARGE': 435,
            'LAVA_PLUME': 436,
            'LEAF_STORM': 437,
            'POWER_WHIP': 438,
            'ROCK_WRECKER': 439,
            'CROSS_POISON': 440,
            'GUNK_SHOT': 441,
            'IRON_HEAD': 442,
            'MAGNET_BOMB': 443,
            'STONE_EDGE': 444,
            'CAPTIVATE': 445,
            'STEALTH_ROCK': 446,
            'GRASS_KNOT': 447,
            'CHATTER': 448,
            'JUDGMENT': 449,
            'BUG_BITE': 450,
            'CHARGE_BEAM': 451,
            'WOOD_HAMMER': 452,
            'AQUA_JET': 453,
            'ATTACK_ORDER': 454,
            'DEFEND_ORDER': 455,
            'HEAL_ORDER': 456,
            'HEAD_SMASH': 457,
            'DOUBLE_HIT': 458,
            'ROAR_OF_TIME': 459,
            'SPACIAL_REND': 460,
            'LUNAR_DANCE': 461,
            'CRUSH_GRIP': 462,
            'MAGMA_STORM': 463,
            'DARK_VOID': 464,
            'SEED_FLARE': 465,
            'OMINOUS_WIND': 466,
            'SHADOW_FORCE': 467,
            'HONE_CLAWS': 468,
            'WIDE_GUARD': 469,
            'GUARD_SPLIT': 470,
            'POWER_SPLIT': 471,
            'WONDER_ROOM': 472,
            'PSYSHOCK': 473,
            'VENOSHOCK': 474,
            'AUTOTOMIZE': 475,
            'RAGE_POWDER': 476,
            'TELEKINESIS': 477,
            'MAGIC_ROOM': 478,
            'SMACK_DOWN': 479,
            'STORM_THROW': 480,
            'FLAME_BURST': 481,
            'SLUDGE_WAVE': 482,
            'QUIVER_DANCE': 483,
            'HEAVY_SLAM': 484,
            'SYNCHRONOISE': 485,
            'ELECTRO_BALL': 486,
            'SOAK': 487,
            'FLAME_CHARGE': 488,
            'COIL': 489,
            'LOW_SWEEP': 490,
            'ACID_SPRAY': 491,
            'FOUL_PLAY': 492,
            'SIMPLE_BEAM': 493,
            'ENTRAINMENT': 494,
            'AFTER_YOU': 495,
            'ROUND': 496,
            'ECHOED_VOICE': 497,
            'CHIP_AWAY': 498,
            'CLEAR_SMOG': 499,
            'STORED_POWER': 500,
            'QUICK_GUARD': 501,
            'ALLY_SWITCH': 502,
            'SCALD': 503,
            'SHELL_SMASH': 504,
            'HEAL_PULSE': 505,
            'HEX': 506,
            'SKY_DROP': 507,
            'SHIFT_GEAR': 508,
            'CIRCLE_THROW': 509,
            'INCINERATE': 510,
            'QUASH': 511,
            'ACROBATICS': 512,
            'REFLECT_TYPE': 513,
            'RETALIATE': 514,
            'FINAL_GAMBIT': 515,
            'BESTOW': 516,
            'INFERNO': 517,
            'WATER_PLEDGE': 518,
            'FIRE_PLEDGE': 519,
            'GRASS_PLEDGE': 520,
            'VOLT_SWITCH': 521,
            'STRUGGLE_BUG': 522,
            'BULLDOZE': 523,
            'FROST_BREATH': 524,
            'DRAGON_TAIL': 525,
            'WORK_UP': 526,
            'ELECTROWEB': 527,
            'WILD_CHARGE': 528,
            'DRILL_RUN': 529,
            'DUAL_CHOP': 530,
            'HEART_STAMP': 531,
            'HORN_LEECH': 532,
            'SACRED_SWORD': 533,
            'RAZOR_SHELL': 534,
            'HEAT_CRASH': 535,
            'LEAF_TORNADO': 536,
            'STEAMROLLER': 537,
            'COTTON_GUARD': 538,
            'NIGHT_DAZE': 539,
            'PSYSTRIKE': 540,
            'TAIL_SLAP': 541,
            'HURRICANE': 542,
            'HEAD_CHARGE': 543,
            'GEAR_GRIND': 544,
            'SEARING_SHOT': 545,
            'TECHNO_BLAST': 546,
            'RELIC_SONG': 547,
            'SECRET_SWORD': 548,
            'GLACIATE': 549,
            'BOLT_STRIKE': 550,
            'BLUE_FLARE': 551,
            'FIERY_DANCE': 552,
            'FREEZE_SHOCK': 553,
            'ICE_BURN': 554,
            'SNARL': 555,
            'ICICLE_CRASH': 556,
            'V_CREATE': 557,
            'FUSION_FLARE': 558,
            'FUSION_BOLT': 559,
            'FLYING_PRESS': 560,
            'MAT_BLOCK': 561,
            'BELCH': 562,
            'ROTOTILLER': 563,
            'STICKY_WEB': 564,
            'FELL_STINGER': 565,
            'PHANTOM_FORCE': 566,
            'TRICK_OR_TREAT': 567,
            'NOBLE_ROAR': 568,
            'ION_DELUGE': 569,
            'PARABOLIC_CHARGE': 570,
            'FORESTS_CURSE': 571,
            'PETAL_BLIZZARD': 572,
            'FREEZE_DRY': 573,
            'DISARMING_VOICE': 574,
            'PARTING_SHOT': 575,
            'TOPSY_TURVY': 576,
            'DRAINING_KISS': 577,
            'CRAFTY_SHIELD': 578,
            'FLOWER_SHIELD': 579,
            'GRASSY_TERRAIN': 580,
            'MISTY_TERRAIN': 581,
            'ELECTRIFY': 582,
            'PLAY_ROUGH': 583,
            'FAIRY_WIND': 584,
            'MOONBLAST': 585,
            'BOOMBURST': 586,
            'FAIRY_LOCK': 587,
            'KINGS_SHIELD': 588,
            'PLAY_NICE': 589,
            'CONFIDE': 590,
            'DIAMOND_STORM': 591,
            'STEAM_ERUPTION': 592,
            'HYPERSPACE_HOLE': 593,
            'WATER_SHURIKEN': 594,
            'MYSTICAL_FIRE': 595,
            'SPIKY_SHIELD': 596,
            'AROMATIC_MIST': 597,
            'EERIE_IMPULSE': 598,
            'VENOM_DRENCH': 599,
            'POWDER': 600,
            'GEOMANCY': 601,
            'MAGNETIC_FLUX': 602,
            'HAPPY_HOUR': 603,
            'ELECTRIC_TERRAIN': 604,
            'DAZZLING_GLEAM': 605,
            'CELEBRATE': 606,
            'HOLD_HANDS': 607,
            'BABY_DOLL_EYES': 608,
            'NUZZLE': 609,
            'HOLD_BACK': 610,
            'INFESTATION': 611,
            'POWER_UP_PUNCH': 612,
            'OBLIVION_WING': 613,
            'THOUSAND_ARROWS': 614,
            'THOUSAND_WAVES': 615,
            'LANDS_WRATH': 616,
            'LIGHT_OF_RUIN': 617,
            'ORIGIN_PULSE': 618,
            'PRECIPICE_BLADES': 619,
            'DRAGON_ASCENT': 620,
            'HYPERSPACE_FURY': 621,
            'BREAKNECK_BLITZ__PHYSICAL': 622,
            'BREAKNECK_BLITZ__SPECIAL': 623,
            'ALL_OUT_PUMMELING__PHYSICAL': 624,
            'ALL_OUT_PUMMELING__SPECIAL': 625,
            'SUPERSONIC_SKYSTRIKE__PHYSICAL': 626,
            'SUPERSONIC_SKYSTRIKE__SPECIAL': 627,
            'ACID_DOWNPOUR__PHYSICAL': 628,
            'ACID_DOWNPOUR__SPECIAL': 629,
            'TECTONIC_RAGE__PHYSICAL': 630,
            'TECTONIC_RAGE__SPECIAL': 631,
            'CONTINENTAL_CRUSH__PHYSICAL': 632,
            'CONTINENTAL_CRUSH__SPECIAL': 633,
            'SAVAGE_SPIN_OUT__PHYSICAL': 634,
            'SAVAGE_SPIN_OUT__SPECIAL': 635,
            'NEVER_ENDING_NIGHTMARE__PHYSICAL': 636,
            'NEVER_ENDING_NIGHTMARE__SPECIAL': 637,
            'CORKSCREW_CRASH__PHYSICAL': 638,
            'CORKSCREW_CRASH__SPECIAL': 639,
            'INFERNO_OVERDRIVE__PHYSICAL': 640,
            'INFERNO_OVERDRIVE__SPECIAL': 641,
            'HYDRO_VORTEX__PHYSICAL': 642,
            'HYDRO_VORTEX__SPECIAL': 643,
            'BLOOM_DOOM__PHYSICAL': 644,
            'BLOOM_DOOM__SPECIAL': 645,
            'GIGAVOLT_HAVOC__PHYSICAL': 646,
            'GIGAVOLT_HAVOC__SPECIAL': 647,
            'SHATTERED_PSYCHE__PHYSICAL': 648,
            'SHATTERED_PSYCHE__SPECIAL': 649,
            'SUBZERO_SLAMMER__PHYSICAL': 650,
            'SUBZERO_SLAMMER__SPECIAL': 651,
            'DEVASTATING_DRAKE__PHYSICAL': 652,
            'DEVASTATING_DRAKE__SPECIAL': 653,
            'BLACK_HOLE_ECLIPSE__PHYSICAL': 654,
            'BLACK_HOLE_ECLIPSE__SPECIAL': 655,
            'TWINKLE_TACKLE__PHYSICAL': 656,
            'TWINKLE_TACKLE__SPECIAL': 657,
            'CATASTROPIKA': 658,
            'SHORE_UP': 659,
            'FIRST_IMPRESSION': 660,
            'BANEFUL_BUNKER': 661,
            'SPIRIT_SHACKLE': 662,
            'DARKEST_LARIAT': 663,
            'SPARKLING_ARIA': 664,
            'ICE_HAMMER': 665,
            'FLORAL_HEALING': 666,
            'HIGH_HORSEPOWER': 667,
            'STRENGTH_SAP': 668,
            'SOLAR_BLADE': 669,
            'LEAFAGE': 670,
            'SPOTLIGHT': 671,
            'TOXIC_THREAD': 672,
            'LASER_FOCUS': 673,
            'GEAR_UP': 674,
            'THROAT_CHOP': 675,
            'POLLEN_PUFF': 676,
            'ANCHOR_SHOT': 677,
            'PSYCHIC_TERRAIN': 678,
            'LUNGE': 679,
            'FIRE_LASH': 680,
            'POWER_TRIP': 681,
            'BURN_UP': 682,
            'SPEED_SWAP': 683,
            'SMART_STRIKE': 684,
            'PURIFY': 685,
            'REVELATION_DANCE': 686,
            'CORE_ENFORCER': 687,
            'TROP_KICK': 688,
            'INSTRUCT': 689,
            'BEAK_BLAST': 690,
            'CLANGING_SCALES': 691,
            'DRAGON_HAMMER': 692,
            'BRUTAL_SWING': 693,
            'AURORA_VEIL': 694,
            'SINISTER_ARROW_RAID': 695,
            'MALICIOUS_MOONSAULT': 696,
            'OCEANIC_OPERETTA': 697,
            'GUARDIAN_OF_ALOLA': 698,
            'SOUL_STEALING_7_STAR_STRIKE': 699,
            'STOKED_SPARKSURFER': 700,
            'PULVERIZING_PANCAKE': 701,
            'EXTREME_EVOBOOST': 702,
            'GENESIS_SUPERNOVA': 703,
            'SHELL_TRAP': 704,
            'FLEUR_CANNON': 705,
            'PSYCHIC_FANGS': 706,
            'STOMPING_TANTRUM': 707,
            'SHADOW_BONE': 708,
            'ACCELEROCK': 709,
            'LIQUIDATION': 710,
            'PRISMATIC_LASER': 711,
            'SPECTRAL_THIEF': 712,
            'SUNSTEEL_STRIKE': 713,
            'MOONGEIST_BEAM': 714,
            'TEARFUL_LOOK': 715,
            'ZING_ZAP': 716,
            'NATURES_MADNESS': 717,
            'MULTI_ATTACK': 718,
            'TEN_MILLION_VOLT_THUNDERBOLT': 719,
            'MIND_BLOWN': 720,
            'PLASMA_FISTS': 721,
            'PHOTON_GEYSER': 722,
            'LIGHT_THAT_BURNS_THE_SKY': 723,
            'SEARING_SUNRAZE_SMASH': 724,
            'MENACING_MOONRAZE_MAELSTROM': 725,
            'LETS_SNUGGLE_FOREVER': 726,
            'SPLINTERED_STORMSHARDS': 727,
            'CLANGOROUS_SOULBLAZE': 728,
            'ZIPPY_ZAP': 729,
            'SPLISHY_SPLASH': 730,
            'FLOATY_FALL': 731,
            'PIKA_PAPOW': 732,
            'BOUNCY_BUBBLE': 733,
            'BUZZY_BUZZ': 734,
            'SIZZLY_SLIDE': 735,
            'GLITZY_GLOW': 736,
            'BADDY_BAD': 737,
            'SAPPY_SEED': 738,
            'FREEZY_FROST': 739,
            'SPARKLY_SWIRL': 740,
            'VEEVEE_VOLLEY': 741,
            'DOUBLE_IRON_BASH': 742,
            'MAX_GUARD': 743,
            'DYNAMAX_CANNON': 744,
            'SNIPE_SHOT': 745,
            'JAW_LOCK': 746,
            'STUFF_CHEEKS': 747,
            'NO_RETREAT': 748,
            'TAR_SHOT': 749,
            'MAGIC_POWDER': 750,
            'DRAGON_DARTS': 751,
            'TEATIME': 752,
            'OCTOLOCK': 753,
            'BOLT_BEAK': 754,
            'FISHIOUS_REND': 755,
            'COURT_CHANGE': 756,
            'MAX_FLARE': 757,
            'MAX_FLUTTERBY': 758,
            'MAX_LIGHTNING': 759,
            'MAX_STRIKE': 760,
            'MAX_KNUCKLE': 761,
            'MAX_PHANTASM': 762,
            'MAX_HAILSTORM': 763,
            'MAX_OOZE': 764,
            'MAX_GEYSER': 765,
            'MAX_AIRSTREAM': 766,
            'MAX_STARFALL': 767,
            'MAX_WYRMWIND': 768,
            'MAX_MINDSTORM': 769,
            'MAX_ROCKFALL': 770,
            'MAX_QUAKE': 771,
            'MAX_DARKNESS': 772,
            'MAX_OVERGROWTH': 773,
            'MAX_STEELSPIKE': 774,
            'CLANGOROUS_SOUL': 775,
            'BODY_PRESS': 776,
            'DECORATE': 777,
            'DRUM_BEATING': 778,
            'SNAP_TRAP': 779,
            'PYRO_BALL': 780,
            'BEHEMOTH_BLADE': 781,
            'BEHEMOTH_BASH': 782,
            'AURA_WHEEL': 783,
            'BREAKING_SWIPE': 784,
            'BRANCH_POKE': 785,
            'OVERDRIVE': 786,
            'APPLE_ACID': 787,
            'GRAV_APPLE': 788,
            'SPIRIT_BREAK': 789,
            'STRANGE_STEAM': 790,
            'LIFE_DEW': 791,
            'OBSTRUCT': 792,
            'FALSE_SURRENDER': 793,
            'METEOR_ASSAULT': 794,
            'ETERNABEAM': 795,
            'STEEL_BEAM': 796,
            'EXPANDING_FORCE': 797,
            'STEEL_ROLLER': 798,
            'SCALE_SHOT': 799,
            'METEOR_BEAM': 800,
            'SHELL_SIDE_ARM': 801,
            'MISTY_EXPLOSION': 802,
            'GRASSY_GLIDE': 803,
            'RISING_VOLTAGE': 804,
            'TERRAIN_PULSE': 805,
            'SKITTER_SMACK': 806,
            'BURNING_JEALOUSY': 807,
            'LASH_OUT': 808,
            'POLTERGEIST': 809,
            'CORROSIVE_GAS': 810,
            'COACHING': 811,
            'FLIP_TURN': 812,
            'TRIPLE_AXEL': 813,
            'DUAL_WINGBEAT': 814,
            'SCORCHING_SANDS': 815,
            'JUNGLE_HEALING': 816,
            'WICKED_BLOW': 817,
            'SURGING_STRIKES': 818,
            'THUNDER_CAGE': 819,
            'DRAGON_ENERGY': 820,
            'FREEZING_GLARE': 821,
            'FIERY_WRATH': 822,
            'THUNDEROUS_KICK': 823,
            'GLACIAL_LANCE': 824,
            'ASTRAL_BARRAGE': 825,
            'EERIE_SPELL': 826,
            'DIRE_CLAW': 827,
            'PSYSHIELD_BASH': 828,
            'POWER_SHIFT': 829,
            'STONE_AXE': 830,
            'SPRINGTIDE_STORM': 831,
            'MYSTICAL_POWER': 832,
            'RAGING_FURY': 833,
            'WAVE_CRASH': 834,
            'CHLOROBLAST': 835,
            'MOUNTAIN_GALE': 836,
            'VICTORY_DANCE': 837,
            'HEADLONG_RUSH': 838,
            'BARB_BARRAGE': 839,
            'ESPER_WING': 840,
            'BITTER_MALICE': 841,
            'SHELTER': 842,
            'TRIPLE_ARROWS': 843,
            'INFERNAL_PARADE': 844,
            'CEASELESS_EDGE': 845,
            'BLEAKWIND_STORM': 846,
            'WILDBOLT_STORM': 847,
            'SANDSEAR_STORM': 848,
            'LUNAR_BLESSING': 849,
            'TAKE_HEART': 850,
            'TERA_BLAST': 851,
            'SILK_TRAP': 852,
            'AXE_KICK': 853,
            'LAST_RESPECTS': 854,
            'LUMINA_CRASH': 855,
            'ORDER_UP': 856,
            'JET_PUNCH': 857,
            'SPICY_EXTRACT': 858,
            'SPIN_OUT': 859,
            'POPULATION_BOMB': 860,
            'ICE_SPINNER': 861,
            'GLAIVE_RUSH': 862,
            'REVIVAL_BLESSING': 863,
            'SALT_CURE': 864,
            'TRIPLE_DIVE': 865,
            'MORTAL_SPIN': 866,
            'DOODLE': 867,
            'FILLET_AWAY': 868,
            'KOWTOW_CLEAVE': 869,
            'FLOWER_TRICK': 870,
            'TORCH_SONG': 871,
            'AQUA_STEP': 872,
            'RAGING_BULL': 873,
            'MAKE_IT_RAIN': 874,
            'PSYBLADE': 875,
            'HYDRO_STEAM': 876,
            'RUINATION': 877,
            'COLLISION_COURSE': 878,
            'ELECTRO_DRIFT': 879,
            'SHED_TAIL': 880,
            'CHILLY_RECEPTION': 881,
            'TIDY_UP': 882,
            'SNOWSCAPE': 883,
            'POUNCE': 884,
            'TRAILBLAZE': 885,
            'CHILLING_WATER': 886,
            'HYPER_DRILL': 887,
            'TWIN_BEAM': 888,
            'RAGE_FIST': 889,
            'ARMOR_CANNON': 890,
            'BITTER_BLADE': 891,
            'DOUBLE_SHOCK': 892,
            'GIGATON_HAMMER': 893,
            'COMEUPPANCE': 894,
            'AQUA_CUTTER': 895,
            'BLAZING_TORQUE': 896,
            'WICKED_TORQUE': 897,
            'NOXIOUS_TORQUE': 898,
            'COMBAT_TORQUE': 899,
            'MAGICAL_TORQUE': 900,
            'BLOOD_MOON': 901,
            'MATCHA_GOTCHA': 902,
            'SYRUP_BOMB': 903,
            'IVY_CUDGEL': 904,
            'ELECTRO_SHOT': 905,
            'TERA_STARSTORM': 906,
            'FICKLE_BEAM': 907,
            'BURNING_BULWARK': 908,
            'THUNDERCLAP': 909,
            'MIGHTY_CLEAVE': 910,
            'TACHYON_CUTTER': 911,
            'HARD_PRESS': 912,
            'DRAGON_CHEER': 913,
            'ALLURING_VOICE': 914,
            'TEMPER_FLARE': 915,
            'SUPERCELL_SLAM': 916,
            'PSYCHIC_NOISE': 917,
            'UPPER_HAND': 918,
            'MALIGNANT_CHAIN': 919,
        },
    }
