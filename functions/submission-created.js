require("dotenv").config();
const gitpush = require('./github');

const { BASE_URL } = process.env;

exports.handler = async (event, context, callback) => {
  const data = JSON.parse(event.body).payload
  await gitpush(data).then(
    result => {
      callback(null, {
        statusCode: 200,
        body: JSON.stringify({ message: result })
      })
  })
}
