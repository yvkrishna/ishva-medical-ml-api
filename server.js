const express = require("express");
const cors = require("cors");
const app = express();
var bodyParser = require('body-parser');
const { spawn } = require('child_process');
// const py = spawn('python', ['risk_estimation.py']);

// py.stdout.on('data', (data) => {
// 	console.log(data.toString());
// });

// py.on('close', (code) => {
// 	console.log(`child process exited with code ${code}`)
// });

app.use(cors())

app.get('/',function(req, res) {
	res.send("Hello Vedha Krishna");
});

app.get('/getRiskScore',function(req, res) {
	const py = spawn('python', ['risk_estimation.py']);

	py.stdout.on('data', (data) => {
		var val = data.toString()
		res.send(JSON.parse(val))
	});
	
	py.on('close', (code) => {
		console.log(`child process exited with code ${code}`)
	});
});

app.get('/getSurvivalScore',function(req, res) {
	const py = spawn('python', ['survival_estimation.py']);

	py.stdout.on('data', (data) => {
		var val = data.toString()
		res.send(JSON.parse(val))
	});
	
	py.on('close', (code) => {
		console.log(`child process exited with code ${code}`)
	});
});

app.get('/getHazardScore',function(req, res) {
	const py = spawn('python', ['hazard_estimation.py']);

	py.stdout.on('data', (data) => {
		var val = data.toString()
		res.send(JSON.parse(val))
	});
	
	py.on('close', (code) => {
		console.log(`child process exited with code ${code}`)
	});
});

app.set('port',process.env.PORT||5000)

var server = app.listen(app.get('port'),function(){
console.log("server started at port "+app.get('port').toString())
})