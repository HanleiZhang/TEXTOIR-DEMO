from open_intent_detection.init_parameters import Param as param1
from open_intent_discovery.init_parameters import Param as param2

from dataloader import *
from utils import debug

def run():

    print('Open Intent Discovery Begin...')
    
    print('Parameters Initialization...')
    param = Param()
    args = param.args 

    print('Data Preparation...')
    data = Data(args)

    Method = __import__('methods.' + args.method + '.manager')
    Method = Method.__dict__[args.method].manager
    manager = Method.ModelManager(args, data)

    print('Training Begin...')
    manager.train(args, data)
    print('Training Finished...')

    print('Evaluation begin...')
    manager.evaluation(args, data)
    print('Evaluation finished...')

    debug(data, manager, args)
    print('Open Intent Discovery Finished...')

if __name__ == '__main__':
    run()