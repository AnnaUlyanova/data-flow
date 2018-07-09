import {
   compose,
   lifecycle,
   withStateHandlers,
 } from 'recompose'

 import {
   keys,
   map,
   propOr,
   find,
   prop,
   pathOr,
   flatten,
   values
 } from 'ramda'

 import { expensesByCategories, getYears } from '../main-data'
 import ByCategory from '../components/ByCategory'

 const getCategories = expensesByCategories.then((data) => keys(data))

 export const enhance = compose(
   lifecycle({
     componentDidMount(){
       getCategories.then((categories) => {
         this.setState({
           categories: categories
         })
       })
       expensesByCategories.then((allCategoriesData) => {
         this.setState({
           allCategoriesData: allCategoriesData
         })
       })
      }
   }),
   withStateHandlers(
     ({ initialData = [] }) => ({
       dataForSelectedCategory: initialData
     }),
      { showDataForCategory: ({ dataForSelectedCategory }) => (allCategoriesData, category) => {
         return ({
           yearsForSelectedCategory: flatten(map(keys, pathOr('', ['rent'], allCategoriesData))),
           totalExpensesForSelectedCategory: map(prop('total'), flatten(map(values, propOr('', [category], allCategoriesData)))),
           averageExpensesForSelectedCategory: map(prop('average'), flatten(map(values, propOr('', [category], allCategoriesData)))),
         })
       }
    }
  )
 )

 export default enhance(ByCategory)
