class Verb:
    def __init__(self, term=None, index=None, type=None, category=None, case=None, gender=None, number=None, person=None, tam=None):
        self.term = term
        self.index = index
        self.type = type                    # main, auxiliary, regular
        self.category = category            # v
        self.case = case                    # d, o
        self.gender = gender                # m, f
        self.number = number                # s, p
        self.person = person                # u, m, a, m_h, m_h0, m_h1, m_h2
        self.tam = tam                      # some text
