const fetch = require('node-fetch')

const year2013MonthlyUrl = 'http://0.0.0.0:8080/years_monthly_expenses.json'

const annualExpeneseByMonths = fetch(year2013MonthlyUrl)
  .then((response) => response.json())
  .then((data) => console.log('data: ', data))
  .catch((error) => console.log('error: ', error));

console.log('annualExpeneseByMonths', annualExpeneseByMonths)
