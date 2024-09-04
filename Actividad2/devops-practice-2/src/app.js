const express = require("express");
const app = express();

//Primer endpoint
app.get("/",(request,response)=>{
    response.send("Hello world again!");
});

//exportamos el app como modulo para poder ser usado en otros archivos
module.exports = app; 