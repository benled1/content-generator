# TODO

# Run the service in dev mode:
Run the following command. You can then attach to this container using vscode and edit the code. The edits should be reflected locally.
```
docker compose -f docker-compose.dev.yml up -it
```

## create a service that will take in some data and turn that data into video content.

- need a way to turn text to speech and save as audio file.
- need a way to combine that audio with a boiler plate video. (this boiler plate video should probably be generated before hand (not in content generation step.))

# find the lines of code with this :) 
```
 find . -name '*.py' | xargs wc -l
```

# update the imagemagick policy
https://github.com/Zulko/moviepy/issues/401#issuecomment-278679961


# install font
```
wget https://github.com/sonatype/tycho-book/blob/94b9c94b36e1c3724c0e9621550da19a63e0623f/tycho-pdf/src/fonts/Courier.ttf
```