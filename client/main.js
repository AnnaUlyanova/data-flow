const fetch = require('node-fetch')

const year2013MonthlyUrl = 'http://0.0.0.0:8080/year2013_monthly.json'

const year2013MonthlyExpenses = fetch(year2013MonthlyUrl)
  .then((response) => response.json())
  .then((data) => console.log('data: ', data))
  .catch((error) => console.log('error: ', error));

console.log('year2013MonthlyUrl', year2013MonthlyExpenses)
