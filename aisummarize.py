# Type this into your command line to import in the necessary libraries:
# pip install nltk
# pip install textblob
# pip install newspaper3k


import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():

    url = urlText.get('1.0', "end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state = 'normal')
    author.config(state = 'normal')
    date.config(state = 'normal')
    summary.config(state = 'normal')
    sentiment.config(state = 'normal')
    
    title.delete('1.0', "end")
    title.insert('1.0', article.title)

    author.delete('1.0', "end")
    author.insert('1.0', article.authors)

    date.delete('1.0', "end")
    date.insert('1.0', article.publish_date)

    summary.delete('1.0', "end")
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', "end")
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')
    title.config(state = 'disabled')
    author.config(state = 'disabled')
    date.config(state = 'disabled')
    summary.config(state = 'disabled')
    sentiment.config(state = 'disabled')



root = tk.Tk()
root.title("News Summarizer")
root.geometry('1600x800')

titleLabel = tk.Label(root, text="Title")
titleLabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg = '#dddddd')
title.pack()

authorLabel = tk.Label(root, text="Author")
authorLabel.pack()

author = tk.Text(root, height=1, width = 140)
author.config(state='disabled', bg = '#dddddd')
author.pack()

dateLabel = tk.Label(root, text="Publication Date")
dateLabel.pack()

date = tk.Text(root, height=1, width = 140)
date.config(state='disabled', bg = '#dddddd')
date.pack()

summaryLabel = tk.Label(root, text="Summary")
summaryLabel.pack()

summary = tk.Text(root, height=25, width = 170)
summary.config(state='disabled', bg = '#dddddd')
summary.pack()

sentimentLabel = tk.Label(root, text="Sentiment")
sentimentLabel.pack()

sentiment = tk.Text(root, height=1, width = 140)
sentiment.config(state='disabled', bg = '#dddddd')
sentiment.pack()

urlLabel = tk.Label(root, text="Enter The URL For The Website You Want To Analyze")
urlLabel.pack()

urlText = tk.Text(root, height=1, width = 140)
urlText.pack()

button = tk.Button(root, text = "Summarize!", command  = summarize)
button.pack()
root.mainloop()