const app = require("./app");

// Nuestro servidor iniciará en el puerto 3000
const port = process.env.PORT||3000;

app.listen(port,()=>{
    console.log("Server running on port: %i",3000);
});