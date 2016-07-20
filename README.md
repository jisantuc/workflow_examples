Workflow Examples
=================

There are two examples contained here:

- wordcount: a simple wordcount example that does an `s3` file upload for no real reason first
- sleepy: a simple demonstration of concurrent task execution

Before you run either, install the requirements and then run `luigid` from a shell anywhere you like.

For both, viewing the luigi visualizer at `localhost:8082` is at least one of helpful or fun. (It [doesn't autorefresh](https://github.com/spotify/luigi/issues/1622), so keep your finger on that \<F5\> button)

Either example can be done with `docker build <dirname>`, and directions for running outside of docker containers are below.

Wordcount
---------

To run this example, you'll need three pretty standard things and one thing of your own choosing:

- AWS creds exported as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` so you can upload things to `s3`
- `scala` / `sbt` installed
- `pip install -r requirements.txt`
- some text file to play with. I picked [_Frankenstein_](http://www.gutenberg.org/cache/epub/84/pg84.txt)

After that's true, `cd` to `wordcount`, run `sbt package`, then `PYTHONPATH='' luigi CountWords --module wordcount --input-file your-txt-file-here.txt`

SleepyTime
----------

To run this example, cd to `sleepy` and `python runner.py` while refreshing the visualizer to watch scheduling happen. You'll have a bunch of pending jobs and bunch of running jobs and probably a lot of trouble containing your excitement.
