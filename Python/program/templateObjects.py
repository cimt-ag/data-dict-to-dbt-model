class Hub:
    def __init__(self, src_pk, src_nk, src_ldts=None, src_source=None):
        self.src_pk = src_pk
        self.src_nk = src_nk
        self.src_ldts = src_ldts
        self.src_source = src_source

class Stage:
    def __init__(self, meta_rec_src, src_nk):
        self.meta_rec_src = meta_rec_src
        self.src_nk = src_nk

    def printSelf(self):
        print(self.meta_rec_src)
        print(self.src_nk)