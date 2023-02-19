class Pokemon:
    def __init__(self, pokeid):

        #Pokédex data
        self.pokeid = pokeid
        self.num = None
        self.name = None
        self.type = None
        self.species = None
        self.height = None
        self.weight = None
        self.abilities = []
        self.local_num = None

        #Appearance data
        self.img = None
        self.colors = []

        #Base stats
        self.hp = None
        self.atk = None
        self.defense = None
        self.spa = None
        self.spd = None
        self.spe = None
        self.tot = None

        #Training data
        self.ev_yield = None
        self.catch_rate = None
        self.base_friendship = None
        self.base_experience = None
        self.growth_rate = None

        #Breeding data
        self.egg_group = []
        self.gender_ratio = None
        self.egg_cycles = None

        #Evolution data
        self.evo_tree = None
        self.evo_methods = []
        self.direct_evos = []