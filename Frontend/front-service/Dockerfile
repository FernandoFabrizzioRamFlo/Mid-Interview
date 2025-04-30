# Versión ligera de Node LTS
FROM node:22.15.0-alpine
WORKDIR /Frontend/front-service
# Copia los archivos de configuración e instala dependencias
COPY package.json package-lock.json ./
RUN npm install
COPY . .

EXPOSE 4000
#problemas de configuraciones de next impiden ejecutar build. Se opta por ejecutar dev como prototipo. 
CMD ["npm", "run", "dev"]