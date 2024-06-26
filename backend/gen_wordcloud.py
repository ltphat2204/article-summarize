from normalize import process
from underthesea import pos_tag, word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from underthesea import pos_tag

def generateWordCloud(text):
    content = process(text)
    preprocessed_data_in_sentences = word_tokenize(content, format="text")
    wordcloud = WordCloud(width = 1100, height = 500, background_color='white', min_font_size=10).generate(preprocessed_data_in_sentences)
    plt.figure(figsize = (11, 5), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    return plt
