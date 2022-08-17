#!/usr/bin/node

const axios = require('axios');

async function makeRequest () {
  const data = await axios.get(process.argv[2]);
  console.log('code:', data.status);
}

makeRequest();
