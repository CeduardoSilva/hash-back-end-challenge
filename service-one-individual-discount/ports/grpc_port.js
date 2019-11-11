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
async function individualDiscount(call, callback) {
  var discountReply = await controller.individualDiscount(call.request);
  
  // Trying to parse shit
  discountReply.applicable_discounts = JSON.stringify(discountReply.applicable_discounts);
  discountReply.pct = parseFloat(discountReply.pct);
  discountReply.value_in_cents = parseInt(discountReply.value_in_cents);
  
  console.log(`Discount: ${JSON.stringify(discountReply)}`);
  console.log(`pct: ${typeof discountReply.pct}`);
  console.log(`value_in_cents: ${typeof discountReply.value_in_cents}`);
  console.log(`applicable_discounts: ${typeof discountReply.applicable_discounts}`);

  callback(null,discountReply);
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