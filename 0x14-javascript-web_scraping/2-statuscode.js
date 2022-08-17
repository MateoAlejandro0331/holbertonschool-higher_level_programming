#!/usr/bin/node

const axios = require('axios');

async function makeRequest () {
  try {
    const data = await axios.get(process.argv[2]);
    console.log(data.status);
  } catch (err) {
    if (err.response) {
      // ✅ log status code here
      console.log(err.response.status);
    }
  }
}

makeRequest();
