FROM node:18-slim

WORKDIR /app

COPY package*.json ./

RUN npm install --only=production

COPY . .

EXPOSE 5004

CMD ["node", "app.js"]