var PROTO_PATH = __dirname + '/../protos/individualdiscount.proto';

var _ = require('lodash');
var controller = require('../controller/controller');
var grpc = require('grpc');
var protoLoader = require('@grpc/proto-loader');
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });
var individual_discount_proto = grpc.loadPackageDefinition(packageDefinition).individualdiscount;
var grpcconfig = require('../config/grpcconfig.json');

/**
 * Manage the streaming between gRPC client and server
 * @param {individualDiscountRequest} call 
 */
function individualDiscountStream(call) {
  
  var requestsList = [];

  call.on('data', (individualDiscountRequest) => {
    requestsList.push(individualDiscountRequest);
  });
  call.on('end', function() {
    var count = 0;
    _.each(requestsList, (request) => {
      controller.individualDiscount(request).then(discountReply => {
        call.write(discountReply);
        count++;
        if(count == requestsList.length) call.end();
      }).catch(e => {
        call.write(e);
        count++;
        if(count == requestsList.length) call.end();
      });
    });
  });
}

/**
 * Create the gRPC server instance
 * @return {Object} server
 */
function getServer() {
  var server = new grpc.Server();
  server.addService(individual_discount_proto.Discount.service, {
    individualDiscountStream: individualDiscountStream
  });
  return server;
}

/**
 * Set the server up and starts it
 */
function startServer() {
  var server = new getServer();
  server.bind(grpcconfig.url, grpc.ServerCredentials.createInsecure());
  server.start();
  console.log('gRPC Server started');
}

module.exports = {
  individualDiscountStream: individualDiscountStream,
  startServer: startServer
}