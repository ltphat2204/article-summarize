from normalize import process
from underthesea import pos_tag
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from underthesea import pos_tag

def generateWordCloud(text):
    content = process(text)
    content_with_tag = pos_tag(content)
    content_with_tag = list(filter(lambda word: word[1] in ['V', 'A', 'N'], content_with_tag))
    preprocessed_data_in_sentences = ' '.join('_'.join(word[0].split(' ')) for word in content_with_tag)
    wordcloud = WordCloud(width = 1100, height = 500, background_color='white', min_font_size=10).generate(preprocessed_data_in_sentences)
    plt.figure(figsize = (11, 5), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    return plt
