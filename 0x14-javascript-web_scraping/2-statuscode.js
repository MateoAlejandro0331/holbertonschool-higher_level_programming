#!/usr/bin/node

const axios = require('axios');

async function makeRequest () {
  try {
    const res = await axios.get(process.argv[2]);
    console.log('code:', res.status);
  } catch (err) {
    if (err.response) {
      // ✅ log status code here
      console.log('code:', err.response.status);
    }
  }
}

makeRequest();
