const fetch = require('node-fetch')

const yearsMonthlyExpensesUrl = 'http://localhost:8080/years_monthly_expenses.json'

export const annualExpeneseByMonths = fetch(yearsMonthlyExpensesUrl)
  .then((response) => response.json())
  .catch((error) => console.log('error: ', error))
  
