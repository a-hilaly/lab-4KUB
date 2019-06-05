FROM node

ADD server.js .

ADD package.json .

RUN npm i

ENTRYPOINT [ "npm", "start" ]