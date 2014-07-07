var fs     = require('fs');
var file   = process.argv.slice(2)[0];
var args   = JSON.parse(fs.readFileSync(file, 'utf-8')); 

var Manana = require(args.interpreter);
var manana = new Manana.Manana(args.view_dir);

var res = manana[args.method](args.view, args.context);

fs.unlink(file, function(err) {
  if (err) {
    throw err;
  }
});

console.log(res);
