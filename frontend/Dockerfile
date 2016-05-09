FROM node:6.1-onbuild

RUN npm install webpack -g

ADD package.json /frontend/package.json
#ADD webpack.config.js /frontend/webpack.config.js

WORKDIR /frontend
RUN npm install

ADD . /frontend
CMD exec webpack -p