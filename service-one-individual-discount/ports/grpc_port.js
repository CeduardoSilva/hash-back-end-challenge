var PROTO_PATH = __dirname + '/../../protos/individualdiscount.proto';

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

/**  
 * Tries to implement the stream
*/
function individualDiscountStream(call) {
  call.on('data', function(individualDiscountRequest) {
    controller.individualDiscount(individualDiscountRequest).then(discountReply => {
      console.log(`Discount: ${JSON.stringify(discountReply)}`);
      call.write(discountReply);
      console.log("Written...")
    }).catch(e => {
      console.log(`Couldn't calculate discount`);
      call.write(e);
    });
  });
  call.on('end', function() {
    console.log("ENDED");
    call.end();
  });
}

/**
 * Implements the Individual Discount RPC method.
 */
function individualDiscount(call, callback) {

  controller.individualDiscount(call.request).then(discountReply => {
    console.log(`Discount: ${JSON.stringify(discountReply)}`);
    callback(null,discountReply);
  }).catch(e => {    
    console.log(`Couldn't calculate discount`);
    callback(null,e);
  })
  
}

function getServer() {
  var server = new grpc.Server();
  server.addService(individual_discount_proto.Discount.service, {
    individualDiscountStream: individualDiscountStream,
    individualDiscount: individualDiscount
  });
  return server;
}

/**
 * Starts an RPC server that receives requests for the Individual Discount service at the
 * sample server port
 */
function main() {
  var server = new getServer();
  server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
  server.start();
}

main();