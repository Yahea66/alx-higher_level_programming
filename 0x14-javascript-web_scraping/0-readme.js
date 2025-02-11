#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

try {
  const data = fs.readFileSync(filePath, 'utf-8');
  console.log(data);
} catch (error) {
  console.error(error);
  process.exit(1);
}
