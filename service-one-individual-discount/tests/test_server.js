/*
 *
 * Copyright 2015 gRPC authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

var PROTO_PATH = __dirname + '/../protos/individualdiscount.proto';

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
 * Functions to implement the bussiness logic
 */
// Returns today's date formatted as MM/DD/YYYY
function nowDate() {
  var now = new Date();
  var y = now.getFullYear();
  var m = now.getMonth() + 1;
  var d = now.getDate();
  return '' + (m < 10 ? '0' : '') + m + '/' + (d < 10 ? '0' : '') + d  + '/' + y;
}
// Receives a user's birthday and checks if it is today. 
function isBirthday(userBirthday) {
  return userBirthday.substring(0,5) == nowDate().substring(0,5) ? true : false;
}

/**
 * Implements the SayHello RPC method.
 */
function individualDiscount(call, callback) {
  console.log(JSON.stringify(call.request));
  callback(null, {discount: '10%'});
}

/**
 * Starts an RPC server that receives requests for the Greeter service at the
 * sample server port
 */
function main() {
  var server = new grpc.Server();
  server.addService(individual_discount_proto.Discount.service, {individualDiscount: individualDiscount});
  server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
  server.start();
}

//main();
console.log(isBirthday('11/07/2023'));