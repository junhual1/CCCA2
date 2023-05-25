FROM node:lts-alpine

# COPY mastodon /app/
COPY . /app/

WORKDIR /app

RUN npm config set legacy-peer-deps true
RUN npm install
# RUN apk add yarn
# RUN yarn global add @vue/cli @vue/cli-service-global


CMD [ "npm", "run", "serve" ]
