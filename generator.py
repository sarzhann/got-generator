from transformers import pipeline
got = pipeline('text-generation', model='./gpt2-got', tokenizer='gpt2', config={'max_length':1000})
loop = "Y"
while loop == "Y":
    SOS = input('Input start of the sentence\n\t')
    generated_text = got(SOS)[0]['generated_text']
    print('Generated text:\n\t',generated_text)
    loop = input('If you want to continue type "Y", otherwise type "N"\n\t')