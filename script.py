import torch
import torchtext
from torchtext.legacy.datasets import Multi30k
import spacy
from torchtext.legacy.data import Field, BucketIterator

spacy_de = spacy.load('de_core_news_sm')
spacy_en = spacy.load('en_core_web_sm')

def tokenize_de(text):
    return [tok.text for tok in spacy_de.tokenizer(text)][::-1]
def tokenize_en(text):
    return [tok.text for tok in spacy_en.tokenizer(text)][::-1]

SRC = Field(tokenize = tokenize_de,
           init_token = '<sos>',
           eos_token = '<eos>',
           lower = True)
TRG = Field(tokenize = tokenize_en,
           init_token = '<sos>',
           eos_token = '<eos>',
           lower = True)

train_data, valid_data, test_data = Multi30k.splits(exts=('.de', '.en'),
                                                   fields=(SRC, TRG))

SRC.build_vocab(train_data, min_freq = 2)
TRG.build_vocab(train_data, min_freq = 2)

device = torch.device('cpu')
BATCH_SIZE = 128
train_iterator, valid_iterator, test_iterator = BucketIterator.splits((train_data, valid_data, test_data),
                                                                     batch_size = BATCH_SIZE,
                                                                     device=device)

print("Done")
