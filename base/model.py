import os
import sys
import torch
from config import ActivityConfig as cfg
from ModelZoo import *

class Model(object):
    def __init__(self):
        pass
    def select_model(self,name):
        model =  None
        if name in cfg.MODEL_LIST:
            if name == 'tsn':
                model = TSN(cfg.DATASET.CLASS_NUM,
                            cfg.TRAIN.SEG_NUM ,
                            cfg.TRAIN.MODALITY,
                            base_model=cfg.BACKBONE,
                            new_length=1,
                            consensus_type='avg',
                            before_softmax=True,
                            dropout=cfg.TRAIN.DROPOUT,
                            crop_num=cfg.TRAIN.CROP_NUM,
                            partial_bn=cfg.TRAIN.PARTIAL_BN,
                            pretrain=cfg.PRETRAIN_TYPE)

        else:
            print("=> %s is not in model_list"%(name))
            sys.exit(0)

        return model

if __name__ == '__main__':
    ## uint test
    _model = Model()
    x = torch.randn([1,15,224,224])
    net = _model.select_model('tsn')
    out = net(x)
    print(out)