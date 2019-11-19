const Mocha = require('mocha');
const fs = require('fs');
const path = require('path');
const grpcPort = require('./ports/grpc_port');

var mocha = new Mocha();
var testsDir = './test';

fs.readdirSync(testsDir).filter(function(file) {
    return file.substr(-3) === '.js';
}).forEach(function(file) {
    mocha.addFile(
        path.join(testsDir, file)
    );
});

mocha.run(function(failures) {
  if(failures == 0) {
    console.log('Tests Passed');
    console.log('Starting server...');
    grpcPort.startServer();
  } else {
    throw new Error('Tests failed');
  }
});