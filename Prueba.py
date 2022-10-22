import pandas
url = "kaggle datasets download -d muhammadadiltalay/imdb-video-games"
data = pandas.read_csv(url)
print(data)
