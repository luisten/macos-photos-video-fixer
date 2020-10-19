# Video Fixer for MacOS Photos 
Some video formats aren't recognised properly by MacOS Photos and cannot be imported. Other times, videos might be missing key metadata that the Photos app uses to determine the capture date. This tool helps to fix that.

### Prerequisites
You must have *Python3.5* or later installed locally. You can install it using Homebrew:

```sh
$ brew install python
```

Make sure the version is correct by running:
```sh
$ python --version
```

You must also have *ffmpeg* installed:
```sh
$ brew install ffmpeg
```

### How to use this tool
Create a directory named `input` and copy all the video files you are having trouble with there. Then run the following command:

```sh
$ python main.py
```

The tool will then start processing and converting all the video files to `mp4` and set the creation and modification dates as the capture dates for the video. 

Once the script is done processing the videos, you can import them into the Photos app from the `output` directory.

### Notes
I put this script together after spending hours trying to download and import photos and videos from Google Photos into Apple's Photos app on MacOS. Over the years, I had accumulated videos in all sorts of formats (`3gp`, `mov`, `mpg`, `mpeg`, `avi`, `mp4`, `mts`, `wmv`, etc.) from all sorts of devices (Android phones, iPhones, digital cameras, DSLRs, GoPro, and even Hi8 camcorders).

The first issue I noticed is that a lot of the older files would get imported using the import date as the capture date, even though the file's creation and modification dates were set to years ago.

The second issue was that several file formats were unreadable to the Photos app. This was true for almost all `AVI`, `MTS`, and `WMV` files.

`ffmpeg` will do its best to preserve the video size and quality in the exported files. However, you will notice a reduction in file size especially when converting from `avi` to `mp4`. This is normal and personally, I can't tell if there is any drop in quality.

### Shoutouts
- [Giacomo1968](https://superuser.com/users/167207/giacomo1968) and [drfrogsplat](https://apple.stackexchange.com/users/1587/drfrogsplat) for the tip on changing the [pixel format](https://superuser.com/questions/820134/why-cant-quicktime-play-a-movie-file-encoded-by-ffmpeg) on [stubborn videos](https://apple.stackexchange.com/questions/166553/why-wont-video-from-ffmpeg-show-in-quicktime-imovie-or-quick-preview).
- Stefan Barthel's [photos-date-fixer](https://github.com/brtx/photos-date-fixer) script, which didn't solve the issues I had but made me believe that I could script it myself.