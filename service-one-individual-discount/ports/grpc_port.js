var PROTO_PATH = __dirname + '/../../protos/individualdiscount.proto';

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

// REMOVE AND ADJUST
function individualDiscount(call, callback) {

  controller.individualDiscount(call.request).then(discountReply => {
    callback(null,discountReply);
  }).catch(e => {    
    callback(null,e);
  })
  
}

/**
 * Don't need testing
 */
function getServer() {
  var server = new grpc.Server();
  server.addService(individual_discount_proto.Discount.service, {
    individualDiscountStream: individualDiscountStream,
    individualDiscount: individualDiscount
  });
  return server;
}

/**
 * Dont need testing
 */
function main() {
  var server = new getServer();
  server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
  server.start();
}

main();