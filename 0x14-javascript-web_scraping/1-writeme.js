#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const text = process.argv[3];

try {
  fs.writeFileSync(filePath, text, 'utf-8');
} catch (error) {
  console.error(error);
  process.exit(1);
}
