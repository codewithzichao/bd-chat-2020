#! -*- coding: utf-8 -*-

import sys
import warnings


__version__ = '0.5.8'


class Legacy1:
    """向后兼容
    """
    def __init__(self):
        import bert4keras_5_8.models
        self.models = bert4keras_5_8.models
        self.__all__ = [k for k in dir(self.models) if k[0] != '_']

    def __getattr__(self, attr):
        """使得 from bert4keras_5_8.bert import xxx
        等价于from bert4keras_5_8.models import xxx
        """
        warnings.warn('bert4keras_5_8.bert has been renamed as bert4keras_5_8.models.')
        warnings.warn('please use bert4keras_5_8.models.')
        return getattr(self.models, attr)


Legacy1.__name__ = 'bert4keras_5_8.bert'
sys.modules[Legacy1.__name__] = Legacy1()
del Legacy1


class Legacy2:
    """向后兼容
    """
    def __init__(self):
        import bert4keras_5_8.tokenizers
        self.tokenizers = bert4keras_5_8.tokenizers
        self.__all__ = [k for k in dir(self.tokenizers) if k[0] != '_']

    def __getattr__(self, attr):
        """使得 from bert4keras_5_8.tokenizer import xxx
        等价于from bert4keras_5_8.tokenizers import xxx
        """
        warnings.warn('bert4keras_5_8.tokenizer has been renamed as bert4keras_5_8.tokenizers.')
        warnings.warn('please use bert4keras_5_8.tokenizers.')
        return getattr(self.tokenizers, attr)


Legacy2.__name__ = 'bert4keras_5_8.tokenizer'
sys.modules[Legacy2.__name__] = Legacy2()
del Legacy2
