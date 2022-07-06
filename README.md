# HumanFaces
## Disclaimer
I'm not trying to carry out sexism, ageism or anything else here, this is simply an AI (sorting and generating fake faces) test. The AIs are not made by me!
## What's this?
First, I've generated a few fake faces, which have all been constructed by [this](https://thispersondoesnotexist.com/) site, you might already know. To get the raw image, I simply sent a request to [that](https://thispersondoesnotexist.com/image) site, which simply returns a .jfif file, which can be handled identically to .jpg and .jpeg files.

Having all those files shoved together in one folder, I applied [this](https://github.com/serengil/deepface) python package, to sort between gender and age.

It's about 5,000 faces or something generated in a night, feel free to use it as an AI trainer or similar. 1 in 100 faces seems to be glitched or miscategorized.
## How to use
You'll have to follow the installing instructions of [this](https://github.com/serengil/deepface) repository. The rest is being done by the pre-installed "requests" module of python.
