use("Analysis");

// db.mastertable.findOne()

// db.mastertable.find({scheme:"gpay"})

// db.mastertable.find({status:"SUCCESS"})

// finding total number of transaction on the basis of sucess
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$status",
//             totaltransaction:{$sum:1}
//         }
//     }
// ])

// finding total amount spend on the basis of the status
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$status",
//             totalamount:{$sum:"$amount"}
//         }
//     }
// ])

// finding total no of transaction based on the model
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$model",
//             totaltransaction:{$sum:1}
//         }
//     }
// ])

// finding total amount spend on the basis of the model
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$model",
//             totaltransaction:{$sum:"$amount"}
//         }
//     }
// ])


// finding total no of transaction based on the device id
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$_id_device",
//             totaltransaction:{$sum:1}
//         }
//     }
// ])

// calculating total no of transaction based on the payment type
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$type",
//             totaltransaction:{$sum:1}
//         }
//     }
// ])

// calculating total amount on the basis of device type
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$type",
//             totaltransaction:{$sum:"$amount"}
//         }
//     }
// ])

// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$gpay",
//             totaltransaction:{$sum:1}
//         }
//     }
// ])

// // total amount paid through google pay
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$gpay",
//             totaltransaction:{$sum:"$amount"}
//         }
//     }
// ])

// finding total no of transacion based on the language
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$language",
//             totaltransaction:{$sum:1}
//         }
//     }
// ])

// finding total amount based on the language
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$language",
//             totalamount:{$sum:"$amount"}
//         }
//     }
// ])

// findinf the total no of transaction based on the device is active or not
// db.mastertable.aggregate([
//     {
//         $group:{
//             _id:"$is_active",
//             totaltransaction:{$sum:1}
//         }
//     }
// ])


// db.mastertable.updateMany(
//   { is_active: "yes" },
//   { $set: { is_active: true } }
// )

// db.mastertable.updateMany(
//   { is_active: "True" },
//   { $set: { is_active: true } }
// )

// db.mastertable.updateMany(
//   { is_active: "False" },
//   { $set: { is_active: false } }
// )

// db.mastertable.updateMany(
//   { is_active: "true" },
//   { $set: { is_active: true } }
// )

// calculating total transaction amount

// db.mastertable.aggregate([
//   {
//     $group: {
//       _id: null,
//       totalAmount: {
//         $sum: "$amount"
//       }
//     }
//   }
// ])


// trnsaction which has not used any payment method all
// db.mastertable.find({
//   gpay: null,
//   paytm: null,
//   phonepe: null,
//   bhim: null
// })

// Failed transaction more than 100 rupees
// db.mastertable.find({
//   status: "FAILED",
//   amount: {
//     $gt: 1000
//   }
// })

// top 5 highest transaction 
// db.mastertable.find()
// .sort({ amount: -1 })
// .limit(5)

// // Invalid dates
// db.mastertable.find({
//   created_at_audit: null
// })

// finding the no of transaction in which crated _at audit is null
// db.mastertable.aggregate([
//     {
//         $match:{
//             created_at_audit:null
//         }
//     },{
//         $group:{
//             _id:"$created_at_audit",
//             total_transaction:{$sum:1}
//         }
//     }
// ])

// finding total no of transaction in which created at device is null
// db.mastertable.aggregate([
//     {
//         $match:{
//             created_at_device:null
//         }
//     },{
//         $group:{
//             _id:"$created_at_device",
//             total_transaction:{$sum:1}
//         }
//     }
// ])

