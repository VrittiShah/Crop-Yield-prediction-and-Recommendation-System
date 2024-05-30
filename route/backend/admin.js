let expres = require('express')
let router = expres()


router.get('/',(req,res)=>{
    res.render('../views/backend/admin-file')
})

module.exports = router
