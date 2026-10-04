# a dockerfile NEEDS at least 1 base image to build from, since this proj was in python, our base img is python
# rule of choosing: smallest base image that already contains the environment your app fundamentally needs
FROM node:22-alpine AS frontend-builder

WORKDIR /build
COPY app/static/ts ./app/static/ts
RUN npx --yes esbuild@0.25.5 app/static/ts/ask.ts --bundle --outfile=app/static/js/ask.js

FROM python:3.12-slim

# set working directory in container
WORKDIR /app/recall

# copy dependencies
# takes requirements.txt on my project, copies it into . -> in this case, since my working dir is app/recall, . is just that directory: app/recall/requirements.txt
COPY requirements.txt .  
RUN pip install -r requirements.txt

# copy everything from current local working dir onto image dir
# first dot: \Computer Science\Recall, second dot: /app/recall
COPY . .
COPY --from=frontend-builder /build/app/static/js/ask.js ./app/static/js/ask.js

# each dockerfile can only run 1 of these cmds, this is ran when the image finishes building on the container
# below is 1 singular cmd, space separated by commas as list items, this cmd runs the flask server
# --host=0.0.0.0 allows Flask accept connections coming into the container, --port=8080 makes flask listen on 8080 -> makes 0.0.0.0:8080
CMD [ "flask", "--app", "app:app", "run", "--host=0.0.0.0", "--port=8080" ]
