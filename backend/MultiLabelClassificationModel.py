# Import all libraries
import pandas as pd
import numpy as np
import re

# Huggingface transformers
import transformers
from transformers import BertModel, BertTokenizer, AdamW, get_linear_schedule_with_warmup

import torch
from torch import nn, cuda
from torch.utils.data import DataLoader, Dataset, RandomSampler, SequentialSampler

import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)

device = torch.device("cpu")  # torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

TOPICS = [
    "sortings",
    "strings",
    "greedy",
    "number theory",
    "math",
    "graphs",
    "geometry",
    "data structures",
]

# Encode the tags(labels) in a binary format in order to be used for training
from sklearn.preprocessing import MultiLabelBinarizer
mlb = MultiLabelBinarizer()
mlb.fit([TOPICS])


# Load the model
from CPClassifier import CPClassifier

TRAINED_MODEL_NAME = "model-afected-by-greedies.ckpt"
PATH = f"training/{TRAINED_MODEL_NAME}"
THRESHOLD = 0.4


import nlpBert

class MultiLabelClassificationModel:
  def __init__(self):
    self.model = CPClassifier(
      num_classes = len(TOPICS), 
    )

    self.model = self.model.load_from_checkpoint(PATH)

    # Put model in evaluation mode
    self.model = self.model.to(device) # moving model to cuda
    self.model.eval()

  # convert probabilities into 0 or 1 based on a threshold value
  def classify(self, predictions, threshold):
    y_pred = []
    for pred in predictions:
      y_pred.append([bool(label >= threshold) for label in pred])
    return np.array(y_pred)

  def predict(self, problemStatement):
    # print(problemStatement)
    encoded = nlpBert.tokenize(problemStatement)

    predictions_prob = self.model(encoded['input_ids'], encoded['attention_mask'])
    predictions_prob = torch.sigmoid(predictions_prob)

    predictions_prob = predictions_prob.detach().cpu().numpy()
    
    #predictions for optimal threshold
    predictions = self.classify(predictions_prob, THRESHOLD)
    predictions_prob = [prob for prob, pred in zip(predictions_prob[0], predictions[0]) if pred]

    actual_prediction = mlb.inverse_transform(predictions)
    actual_prediction = np.asarray(actual_prediction[0])

    predition_with_probability = [{
      'topic': topic,
      'probability': round(float(prob * 100), 2),
    } for topic, prob in zip(actual_prediction, predictions_prob)]

    return predition_with_probability

# from dummy import staticProblems
# for i in range(0, 10):
#     print(staticProblems[i]['history'])
#     print(f"Predicted {predict(staticProblems[i]['history'])}")
#     print(f"Real {staticProblems[i]['topics']}")
#     print()

# import random
# for i in random.sample(range(len(staticProblems) // 3), 5):
#     print(staticProblems[i]['url'])
#     print(staticProblems[i]['history'])
#     print(f"Predicted {predict(staticProblems[i]['history'])}")
#     print(f"Real {staticProblems[i]['topics']}")
#     print()
