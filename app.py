from flask import Flask
import subprocess
app = Flask("Minerando")

@app.route("/")
def home():
    spider_name = "news"
    subprocess.check_output(['scrapy', 'crawl', spider_name, "-o", "news.json"])
    with open("news.json") as items_file:
        return items_file.read()



if __name__ == '__main__':
    app.run(debug=True)