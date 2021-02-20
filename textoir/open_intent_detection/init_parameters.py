import argparse
import attr

class Param:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser = self.common_param(parser)
        args = parser.parse_args() 
        print(args.method)

        backbones = {'bert':self.bert, 'bert_norm':self.bert_norm } 
        parser = backbones[args.backbone](parser)

        methods = {'ADB':self.ADB, 'MSP':self.MSP, 'DOC':self.DOC, 'DeepUnk':self.DeepUnk, 'OpenMax':self.OpenMax }
        parser = methods[args.method](parser)

        self.args = parser.parse_args() 

    def common_param(self, parser):
        parser.add_argument("--dataset", default='banking', type=str, 
                            help="The name of the dataset to train selected")
        
        parser.add_argument("--known_cls_ratio", default=0.75, type=float, help="The number of known classes")
        
        parser.add_argument("--labeled_ratio", default=1.0, type=float, help="The ratio of labeled samples in the training set")
        
        parser.add_argument("--method", type=str, default='ADB', help="which method to use")

        parser.add_argument("--backbone", type=str, default='bert', help="which model to use")

        parser.add_argument('--seed', type=int, default=0, help="random seed for initialization")

        parser.add_argument('--type', type=str, default='open_intent_detection', help="Type for methods")

        parser.add_argument("--pipe_results_path", type=str, default='pipe_results', help="the path to save results of pipeline methods")

        parser.add_argument("--num_train_epochs", default=200.0, type=float,
                            help="Total number of training epochs to perform.") 
        
        return parser

    def ADB(self, parser):
        parser.add_argument("--lr_boundary", type=float, default=0.05, help="The learning rate of the decision boundary.")
        
        return parser

    def MSP(self, parser):
        parser.add_argument("--threshold", type=float, default=0.5, help="The probability threshold.")
        
        return parser

    def DOC(self, parser):
        parser.add_argument("--scale", type=float, default=2, help="The scale factor of DOC.")
        
        return parser

    def DeepUnk(self, parser):
        parser.add_argument("--n_neighbors", type=int, default=20, help="The number of neighbors of LOF.")

        parser.add_argument("--contamination", type=float, default=0.05, help="The contamination factor of LOF.")

        return parser

    def OpenMax(self, parser):
        
        parser.add_argument("--weibull_tail_size", type=int, default=20, help="The factor of weibull model.")

        parser.add_argument("--alpharank", type=int, default=10, help="The factor of alpha rank.")

        parser.add_argument("--distance_type", type=str, default='cosine', help="The distance type.")

        parser.add_argument("--threshold", type=float, default=0.5, help="The probability threshold.")

        return parser

    def bert(self, parser):
        ##############Your Location for Pretrained Bert Model#####################
        parser.add_argument("--bert_model", default="/home/zhl/pretrained_models/uncased_L-12_H-768_A-12", type=str, help="The path for the pre-trained bert model.")
        
        parser.add_argument("--data_dir", default='data', type=str,
                            help="The input data dir. Should contain the .csv files (or other data files) for the task.")
        
        parser.add_argument("--save_results_path", type=str, default='outputs', help="the path to save results")

        parser.add_argument("--pretrain", action="store_true", default = 'pretrain', help="Pretrain the model")

        parser.add_argument("--pretrain_dir", default='pretrain_models', type=str, 
                            help="The output directory where the model predictions and checkpoints will be written.") 
        
        parser.add_argument("--max_seq_length", default=None, type=int,
                            help="The maximum total input sequence length after tokenization. Sequences longer "
                                "than this will be truncated, sequences shorter will be padded.")

        parser.add_argument("--feat_dim", default=768, type=int, help="The feature dimension.")

        parser.add_argument("--warmup_proportion", default=0.1, type=float)

        parser.add_argument("--freeze_bert_parameters", action="store_true", default="freeze", help="Freeze the last parameters of BERT")

        parser.add_argument("--save_model", action="store_true", help="save trained-model")

        parser.add_argument("--save_results", action="store_true", help="save test results")
        
        parser.add_argument("--gpu_id", type=str, default='0', help="Select the GPU id")

        parser.add_argument("--lr", default=2e-5, type=float,
                            help="The learning rate of BERT.")    
        
        parser.add_argument("--train_batch_size", default=128, type=int,
                            help="Batch size for training.")
        
        parser.add_argument("--eval_batch_size", default=64, type=int,
                            help="Batch size for evaluation.")    
        
        parser.add_argument("--wait_patient", default=10, type=int,
                            help="Patient steps for Early Stop.")    
        
        return parser

    def bert_norm(self, parser):
        ##############Your Location for Pretrained Bert Model#####################
        parser.add_argument("--bert_model", default="/home/zhl/pretrained_models/uncased_L-12_H-768_A-12", type=str, help="The path for the pre-trained bert model.")
        
        parser.add_argument("--data_dir", default='data', type=str,
                            help="The input data dir. Should contain the .csv files (or other data files) for the task.")
        
        parser.add_argument("--save_results_path", type=str, default='outputs', help="the path to save results")

        parser.add_argument("--pretrain", action="store_true", default = 'pretrain', help="Pretrain the model")

        parser.add_argument("--pretrain_dir", default='pretrain_models', type=str, 
                            help="The output directory where the model predictions and checkpoints will be written.") 
        
        parser.add_argument("--max_seq_length", default=None, type=int,
                            help="The maximum total input sequence length after tokenization. Sequences longer "
                                "than this will be truncated, sequences shorter will be padded.")

        parser.add_argument("--feat_dim", default=768, type=int, help="The feature dimension.")

        parser.add_argument("--warmup_proportion", default=0.1, type=float)

        parser.add_argument("--freeze_bert_parameters", action="store_true", default="freeze", help="Freeze the last parameters of BERT")

        parser.add_argument("--save_model", action="store_true", help="save trained-model")

        parser.add_argument("--save_results", action="store_true", help="save test results")
        
        parser.add_argument("--gpu_id", type=str, default='0', help="Select the GPU id")

        parser.add_argument("--lr", default=2e-5, type=float,
                            help="The learning rate of BERT.")    

        parser.add_argument("--num_train_epochs", default=100.0, type=float,
                            help="Total number of training epochs to perform.") 
        
        parser.add_argument("--train_batch_size", default=128, type=int,
                            help="Batch size for training.")
        
        parser.add_argument("--eval_batch_size", default=64, type=int,
                            help="Batch size for evaluation.")    
        
        parser.add_argument("--wait_patient", default=10, type=int,
                            help="Patient steps for Early Stop.")    
        
        return parser
