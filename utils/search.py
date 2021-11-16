from numpy import argmax, argsort
from tensorflow.keras.preprocessing.sequence import pad_sequences


def greedy_search(model, tokenizer, image, max_length):
    # seed the generation process
    in_text = 'startseq'
    # iterate over the whole length of the sequence
    for i in range(max_length):
        # integer encode input sequence
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        # pad input
        sequence = pad_sequences([sequence], maxlen=max_length)
        # predict next word
        yhat = model.predict([image, sequence], verbose=0)
        # convert probability to integer
        yhat = argmax(yhat)
        # map integer to word
        word = word_for_id(yhat, tokenizer)
        # stop if we cannot map the word
        if word is None:
            break
        # append as input for generating the next word
        in_text += ' ' + word
        # stop if we predict the end of the sequence
        if word == 'endseq':
            break
    return in_text


def beam_search(model, tokenizer, image, max_length, beam_index=3):
    # in_text --> [[idx,prob]] ;prob=0 initially
    in_text = [[tokenizer.texts_to_sequences(['startseq'])[0], 0.0]]
    while len(in_text[0][0]) < max_length:
        tempList = []
        for seq in in_text:
            padded_seq = pad_sequences([seq[0]], maxlen=max_length)
            preds = model.predict([image, padded_seq], verbose=0)
            # Take top (i.e. which have highest probailities) `beam_index` predictions
            top_preds = argsort(preds[0])[-beam_index:]
            # Getting the top `beam_index` predictions and
            for word in top_preds:
                next_seq, prob = seq[0][:], seq[1]
                next_seq.append(word)
                # Update probability
                prob += preds[0][word]
                # Append as input for generating the next word
                tempList.append([next_seq, prob])
        in_text = tempList
        # Sorting according to the probabilities
        in_text = sorted(in_text, reverse=False, key=lambda l: l[1])
        # Take the top words
        in_text = in_text[-beam_index:]
    in_text = in_text[-1][0]
    final_caption_raw = [word_for_id(i, tokenizer) for i in in_text]
    final_caption = []
    for word in final_caption_raw:
        if word == 'endseq':
            break
        else:
            final_caption.append(word)
    final_caption.append('endseq')
    return ' '.join(final_caption)


def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None
