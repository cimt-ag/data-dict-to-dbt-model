class Hub:
    def __init__(
            self,
            src_nk
        ):
        self.src_nk = src_nk

class Stage:
    def __init__(
            self,
            business_key,
            meta_rec_src, 
            meta_job_instance_id=-1,
            meta_encryptionkey_index=0,
        ):
        self.business_key = business_key
        self.meta_rec_src = meta_rec_src
        self.meta_job_instance_id = meta_job_instance_id
        self.meta_encryptionkey_index = meta_encryptionkey_index