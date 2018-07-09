import {
   keys,
   map,
   replace
 } from 'ramda'

import fetch from 'node-fetch'

const yearsMonthlyExpensesUrl = 'http://localhost:8080/years_monthly_expenses.json'
const categoriesExpensesUrl = 'http://localhost:8080/data_categories_expenses.json'

export const annualExpeneseByMonths = fetch(yearsMonthlyExpensesUrl)
  .then((response) => response.json())
  .catch((error) => console.log('error: ', error))

export const getYears = annualExpeneseByMonths.then((data) => map(replace(/year /, ''), keys(data)))

export const expensesByCategories = fetch(categoriesExpensesUrl)
  .then((response) => response.json())
  .catch((error) => console.log('error: ', error))
