from open_intent_detection.utils import *

def l2_norm(input,axis=1):
    norm = torch.norm(input,2,axis,True)
    output = torch.div(input, norm)
    return output
    
class L2_normalization(nn.Module):
    def forward(self, input):
        return l2_norm(input)

class bert(BertPreTrainedModel):
    def __init__(self,config,num_labels):
        super(bert, self).__init__(config)
        self.num_labels = num_labels
        self.bert = BertModel(config)
        self.dense = nn.Linear(config.hidden_size, config.hidden_size)
        self.activation = nn.ReLU()
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.classifier = nn.Linear(config.hidden_size,num_labels)
        self.apply(self.init_bert_weights)

    def forward(self, input_ids = None, token_type_ids = None, attention_mask=None , labels = None,
                feature_ext = False, mode = None, loss_fct = None):

        encoded_layer_12, pooled_output = self.bert(input_ids, token_type_ids, attention_mask, output_all_encoded_layers = True)
        pooled_output = self.dense(encoded_layer_12[-1].mean(dim = 1))
        pooled_output = self.activation(pooled_output)
        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)
        
        
        if feature_ext:
            return pooled_output
        else:
            if mode == 'train':
                loss = loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
                return loss
            else:
                return pooled_output, logits
                    

