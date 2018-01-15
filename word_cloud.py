from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


class Wordcloud(object):

	def make(self):
		d = path.dirname(__file__)

		# Read the whole text.
		text = open(path.join(d, './extra_dict/cut_str.txt')).read()

		# read the mask / color image taken from
		alice_coloring = np.array(Image.open(path.join(d, "./extra_dict/li.png")))
		stopwords = set(STOPWORDS)
		stopwords.add("said")

		wc = WordCloud(font_path="./extra_dict/simhei.ttf",background_color="white", max_words=2000, mask=alice_coloring,
		               stopwords=stopwords, max_font_size=40, random_state=42)
		# generate word cloud
		wc.generate(text)

		# create coloring from image
		image_colors = ImageColorGenerator(alice_coloring)

		# show
		plt.imshow(wc, interpolation="bilinear")
		plt.axis("off")
		plt.figure()
		# recolor wordcloud and show
		# we could also give color_func=image_colors directly in the constructor
		plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
		plt.axis("off")
		plt.figure()
		plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
		plt.axis("off")
		wc.to_file(path.join(d, "./extra_dict/yun.png"))
		plt.show()
