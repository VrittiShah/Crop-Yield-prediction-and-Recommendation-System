let express = require('express')
let dotenv = require('dotenv')

dotenv.config({path:'D:\ipd crop web\config.env'})
let app = express()

app.set('view engine','ejs')
app.use(express.static(__dirname+'/public/'))



app.get('/',(req,res)=>{
    res.send('This is Frontend Page')
})

let admin = require('./route/backend/admin')
app.use('/admin',admin)


app.listen(200,()=>{
    console.log('200 port working')
})
