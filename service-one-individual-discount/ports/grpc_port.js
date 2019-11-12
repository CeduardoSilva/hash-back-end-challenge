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

/**
 * Starts an RPC server that receives requests for the Individual Discount service at the
 * sample server port
 */
function main() {
  var server = new grpc.Server();
  server.addService(individual_discount_proto.Discount.service, {individualDiscount: individualDiscount});
  server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
  server.start();
}

main();