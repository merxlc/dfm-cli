# dfm-cli

## Usage

Download the files, go to the folder the files are in, run

```
python main.py [number of questions] [start url] [time delay]
```

You will be prompted for your email and password to log in to your dfm account. to avoid this, you can put your username and password into the `credentials` file.

the `start url` can be acquired by starting a homework or practice session. It should look something like this:

```
https://www.drfrostmaths.com/do-question.php?aaid=31789719
```

Just copy and paste that in.

Note: you can get banned for using this, especially with a low delay (under 5 seconds) or a high question count (over 100)

# Important

before using, you will probably need to install python, and then run the following commands in your terminal:

```
pip install bs4
pip install requests
```

If there's an error, make sure you logged in correctly and that the url is correct and in the correct format. If it still doesn't work send me a msg
