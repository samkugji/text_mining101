class Corpus:
    """Corpus라는 class는 iter_sent가 True일 때에는 double space로 나눠진 문장들을 출력하며, 
    이 때 len은 해당 fname에 있는 문장의 개수입니다. iter_sent가 False 일 때에는 문서의 개수, 즉 line number가 출력됩니다.
    """
    
    def __init__(self, fname, iter_sent=False):
        self.fname = fname
        self.iter_sent = iter_sent
        self.sent_length = 0
        self.doc_length = 0
        
    def __iter__(self):
        with open(self.fname, encoding="utf-8") as f:
            for doc in f:
                doc = doc.strip()                    
                if not self.iter_sent:
                    yield doc
                    continue
                for sent in doc.split('  '):
                    yield sent
    
    def __len__(self):
        if self.iter_sent:
            if self.sent_length == 0:
                with open(self.fname, encoding='utf-8') as f:
                    for doc in f:
                        self.sent_length += len(doc.strip().split('  '))
            return self.sent_length
        else:
            if self.doc_length == 0:
                with open(self.fname, encoding='utf-8') as f:
                    for num_doc, doc in enumerate(f):
                        continue
                    self.doc_length = (num_doc + 1)
            return self.doc_length
