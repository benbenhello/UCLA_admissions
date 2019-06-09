var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/result', function(req, res, next) {
  console.log(res.body.GRE_Score);
});

module.exports = router;