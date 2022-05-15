import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
import numpy as np
def tm(text,number):
    # pass
    #text = '숨겨진 내용 토니z 토니 토니 화이팅 힘내요 화이팅 힘내 입력'+''
    wordList = text.split()
    worduniq=set(wordList)
    wordCount={}
    mask = Image.new("RGBA",(700,500), (255,255,255))
    im = Image.open('./media/images/heart.png').convert("RGBA")
    x,y = im.size
    mask.paste(im,(0,0,x,y),im)
    mask_arr = np.array(mask)
    for w in worduniq:
        wordCount[w]=wordList.count(w)

    wordcloud = WordCloud(background_color ='white', colormap='autumn',font_path='Cafe24Ohsquare.ttf',
                      max_font_size=300,width = 700, height = 500, mask = mask_arr,
                      prefer_horizontal = True).generate_from_frequencies(wordCount)
    plt.figure(figsize=(6,6))
    plt.imshow(wordcloud)
    plt.axis('off')
    
    #
    plt.savefig(f'./media/images/fig{number}.png', bbox_inches='tight')