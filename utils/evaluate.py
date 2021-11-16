from utils.preprocess import load_set, load_clean_descriptions
from nltk.translate.bleu_score import sentence_bleu


def evaluate(predicted, key):
    test = load_set('./models/Flickr_8k.testImages.txt')
    descriptions = load_clean_descriptions(
        './models/descriptions.txt', test)
    references = [d.split() for d in descriptions[key]]
    predicted = predicted.split()
    print(references)
    print(predicted)
    bleu1 = sentence_bleu(references, predicted, weights=(1.0, 0, 0, 0))
    bleu2 = sentence_bleu(references, predicted, weights=(0.5, 0.5, 0, 0))
    bleu3 = sentence_bleu(references, predicted, weights=(0.3, 0.3, 0.3, 0))
    bleu4 = sentence_bleu(references, predicted,
                          weights=(0.25, 0.25, 0.25, 0.25))

    return str(bleu1), str(bleu2), str(bleu3), str(bleu4)
