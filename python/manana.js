var fs     = require('fs'),
    file   = process.argv.slice(2)[0],
    args   = JSON.parse(fs.readFileSync(file, 'utf-8')), 
    Manana = require(args.interpreter),
    manana = new Manana.Manana(args.view_dir),
    html   = manana.render(args.view, args.context);

fs.unlink(file, function(err) {
  if (err) {
    throw err;
  }
});

console.log(html);
