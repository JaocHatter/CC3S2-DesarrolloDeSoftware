# Partimos a partir de la imágen oficial de node 14
FROM node:14 

WORKDIR /app

# Copiar archivos de requirimiento al contenedor para saber que paquetes necesitamos
COPY package*.json ./

# Descargar paquetes
RUN npm install

#Copias los demás archivos
COPY . .

# Abierto en el puerto 3000
EXPOSE 3000

ENV PORT=3000

CMD ["node","src/app.js"]
